"""Check the planning BOM against its CAD/budget source data."""
import csv
import json
from decimal import Decimal
from pathlib import Path


root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'CAD/reference-parts.json').read_text())
with (root / 'BOM.csv').open(newline='') as source:
    rows = list(csv.DictReader(source))
parts = {part['id']: part for part in data['parts']}
assert len(rows) == len(parts) + 1
assert len({row['ID'] for row in rows}) == len(rows)
totals = {'Core USD': Decimal('0'), 'Full USD': Decimal('0')}
for row in rows[:-1]:
    part = parts[row['ID']]
    assert row['Supplier link'] == part['url']
    assert row['Price basis'] == part['price_basis']
    assert row['Availability'] == part['availability']
    assert row['Checked date'] == data['checked_date']
    assert row['Notes'] == part['notes']
    unit = Decimal(str(part['unit_price']))
    assert Decimal(row['Unit USD']) == unit
    for quantity_field, total_field, source_field in [
        ('Core quantity', 'Core USD', 'core_quantity'),
        ('Full quantity', 'Full USD', 'full_quantity'),
    ]:
        quantity = int(row[quantity_field])
        assert quantity == part[source_field]
        expected = quantity * unit
        assert Decimal(row[total_field]) == expected
        totals[total_field] += expected
assert rows[-1]['ID'] == 'TOTAL'
for field, total in totals.items():
    assert Decimal(rows[-1][field]) == total
print('BOM verified:', ', '.join('%s = $%.2f' % item for item in totals.items()))
