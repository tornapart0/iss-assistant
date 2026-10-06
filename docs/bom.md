# Reference parts and budget

Prices checked 2026-10-05. USD. This is a planning BOM, not a purchase-ready specification.
Core: two controllers and two actuated tentacles. Full: four proposed actuators plus Pi/display.
The full layout is proposed; existing firmware drives one servo per controller, not two.

| ID | Part / model | Core qty | Full qty | Unit USD | Full USD | Price basis / availability |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| E01 | [Espressif ESP32-S3-DevKitC-1-N8R8](https://www.espressif.com/en/products/devkits/esp32-s3-series/esp32-s3-devkitc-1) | 2 | 2 | 15.00 | 30.00 | Manufacturer reference price; obtain a supplier quote; Supplier stock not verified |
| E02 | [TowerPro MG90D; Adafruit 1143](https://www.adafruit.com/product/1143) | 2 | 4 | 9.95 | 39.80 | Listed price; Out of stock at checked supplier |
| E03 | [Adafruit 512 analog joystick kit](https://www.adafruit.com/product/512) | 2 | 2 | 5.95 | 11.90 | Listed price; In stock when checked |
| E04 | [Alpha MF01A-N-221-A01; Adafruit 166](https://www.adafruit.com/product/166) | 2 | 4 | 3.95 | 15.80 | Listed price; In stock when checked |
| E05 | [5 V 4 A supply; Adafruit 1466](https://www.adafruit.com/product/1466) | 1 | 1 | 14.95 | 14.95 | Listed price; Add-to-cart available when checked |
| E06 | [2.1 mm jack to terminal block; Adafruit 368](https://www.adafruit.com/product/368) | 1 | 1 | 2.00 | 2.00 | Listed price; In stock when checked |
| E07 | [10 kilohm axial resistors; one pack](https://www.adafruit.com/category/131) | 1 | 1 | 0.75 | 0.75 | Planning allowance; exact pack not selected; Exact part not selected |
| M01 | [Author's octopus geometry; PETG/TPU choice pending](https://us.store.bambulab.com/collections/filament) | 1 | 1 | 20.00 | 20.00 | Material allocation estimate, not a printing-service quote; Material and print settings not selected |
| M02 | [Line and elastic return trial allowance](https://www.mcmaster.com/cord/) | 1 | 1 | 8.00 | 8.00 | Planning allowance; exact line and return system not selected; Exact parts not selected |
| M03 | [Prototype mounting allowance](https://www.mcmaster.com/screws/) | 1 | 1 | 10.00 | 10.00 | Planning allowance; quantities and sizes not finalized; Exact parts not selected |
| E08 | [Wire, connectors, board and protection allowance](https://www.adafruit.com/category/43) | 1 | 1 | 15.00 | 15.00 | Planning allowance; exact parts and protection rating not selected; Exact parts not selected |
| E09 | [Two data-capable micro-USB cables](https://www.adafruit.com/category/34) | 2 | 2 | 3.00 | 6.00 | Planning allowance; exact cable not selected; Exact parts not selected |
| P01 | [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) | 0 | 1 | 15.00 | 15.00 | Manufacturer reference price; supplier quote needed; Reseller stock not verified |
| P02 | [Adafruit 1770 ILI9341 2.8 inch breakout](https://www.adafruit.com/product/1770) | 0 | 1 | 29.95 | 29.95 | Listed price; In stock when checked |
| P03 | [32 GB microSD card allowance](https://www.raspberrypi.com/products/sd-cards/) | 0 | 1 | 12.00 | 12.00 | Planning allowance; exact stocked card not selected; Exact part not selected |
| P04 | [Separate 5 V 2 A supply; Adafruit 276](https://www.adafruit.com/product/276) | 0 | 1 | 7.95 | 7.95 | Listed price; Add-to-cart available when checked |
| P05 | [2.1 mm barrel to micro-USB power cable allowance](https://www.adafruit.com/category/34) | 0 | 1 | 5.00 | 5.00 | Planning allowance; exact cable not selected; Exact part not selected |
| B01 | Checkout allowance | 1 | 1 | 25.00 | 25.00 | Estimate, not a supplier quote; Checkout required |
| B02 | Spare parts and reprint allowance | 1 | 1 | 20.00 | 20.00 | Estimate; Not applicable |

Core planning total: **$191.40**. Full planning total: **$289.10**.
Both totals include $25 shipping/tax and $20 contingency. Printer and tools are assumed available.
Printed material is an allocation estimate, not the cost of buying whole spools or outsourcing prints.

The MG90D is out of stock at the checked supplier. Do not order a substitute without checking
dimensions, positional control, torque, supply voltage/current, spline and servo travel.
Only specific-product rows with listed prices are supplier prices. Manufacturer references
and allowance rows are not quotes. Category links identify sourcing options, not exact products.
Resolve these rows and obtain a checkout total before requesting funding.

The reference assembly does not model mounts, fasteners, tendon routing, returns, connectors,
cables or power protection. Those allowances are not evidence of a finished mechanical design.
Supplier parts remain their manufacturers' designs. CAD envelopes were constructed from
published dimensions and declared allowances, not copied third-party robot designs.
