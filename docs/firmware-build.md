# Firmware build and wiring

This is the existing single-servo prototype, corrected for the ESP32-S3 stated
in the author's README. It does not control four independent octopus arms or
provide Raspberry Pi/display software. Do not treat those features as complete.

Use Arduino-ESP32 3.3.12 and the `esp32:esp32:esp32s3` board target. The classic
ESP32 remains supported with target `esp32:esp32:esp32`.

```sh
arduino-cli core install esp32:esp32@3.3.12 --additional-urls https://espressif.github.io/arduino-esp32/package_esp32_index.json
arduino-cli compile --fqbn esp32:esp32:esp32s3 firmware/iss_assistant
```

| Connection | ESP32-S3 | Classic ESP32 |
| --- | --- | --- |
| Joystick X | GPIO4 | GPIO34 |
| Joystick Y | GPIO5 | GPIO35 |
| Joystick switch, other terminal to GND | GPIO7 | GPIO27 |
| Analog FSR divider midpoint | GPIO6 | GPIO32 |
| Servo signal | GPIO18 | GPIO18 |

Power the joystick and FSR divider from 3.3 V. Connect the FSR between 3.3 V
and its input pin, and a 10 kilohm resistor between that pin and GND. This
firmware assumes pressure increases the ADC reading. A load cell requires
different interface electronics and code.

The servo needs its own supply at its rated voltage, with GND connected to the
controller GND. Do not power the servo from the board's 3.3 V rail. The exact
servo, supply capacity, current protection, and connectors remain undecided.
The diagram covers the low-voltage prototype circuit, not a finished power design.

`HARDWARE_CONFIGURED` defaults to false: no servo PWM is attached. Before enabling
it, verify wiring, joystick centering, servo pulse limits, and the force threshold
with the tendon disconnected. The threshold is raw ADC, not a calibrated force.
Hold the joystick button to move; Y increases closure and decreases opening.
Excess force blocks closing but permits opening. Releasing the button holds the
last command; it is not a physical power disconnect.

The PWM resolution is 14 bits, which ESP32-S3 supports; the old 16-bit request was
unsupported on ESP32-S3. See [Espressif LEDC documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/ledc.html)
and [ESP32-S3 pins](https://docs.espressif.com/projects/esp-idf/en/v6.0/esp32s3/api-reference/peripherals/gpio.html).

The author's two-controller concept can duplicate this circuit, but quantities
and how two actuators would drive four arms still need to be resolved.
