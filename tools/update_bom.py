"""Regenerate the root CSV after editing CAD/reference-parts.json."""
import csv
import json
from decimal import Decimal
from pathlib import Path


HEADERS = ['ID', 'Part', 'Model', 'Core quantity', 'Full quantity', 'Unit USD',
           'Core USD', 'Full USD', 'Price basis', 'Supplier link', 'Availability',
           'Checked date', 'Notes']


def bom_rows(data):
    rows = []
    core_total = Decimal('0')
    full_total = Decimal('0')
    for part in data['parts']:
        unit = Decimal(str(part['unit_price']))
        core = unit * part['core_quantity']
        full = unit * part['full_quantity']
        rows.append([part['id'], part['name'], part['model'], part['core_quantity'],
                     part['full_quantity'], format(unit, '.2f'), format(core, '.2f'),
                     format(full, '.2f'), part['price_basis'], part['url'],
                     part['availability'], data['checked_date'], part['notes']])
        core_total += core
        full_total += full
    rows.append(['TOTAL', 'Planning budget; not a purchase-ready BOM', 'USD', '', '', '',
                 format(core_total, '.2f'), format(full_total, '.2f'), '', '', '', '', ''])
    return rows


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / 'CAD/reference-parts.json').read_text())
    with (root / 'BOM.csv').open('w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(HEADERS)
        writer.writerows(bom_rows(data))
    print('BOM.csv updated. Also refresh the displayed table/totals in docs/bom.md and the audit.')
