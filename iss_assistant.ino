#include <Arduino.h>

// Draft for classic ESP32 DevKit and Arduino-ESP32 3.x.
// One positional servo controls gripper closure, not the four bending tendons.
// Joystick powered by 3.3 V: X -> GPIO34, Y -> GPIO35, switch -> GPIO27/GND.
// Analog FSR divider: 3.3 V -> FSR -> GPIO32 -> 10k resistor -> GND.
// More force must increase the ADC reading. This is not a load-cell driver.
// Servo signal -> GPIO18. Use its rated external supply and a common ground.
// Keep sensor voltages <= 3.3 V. Set limits with the tendon disconnected first.
constexpr int JOY_X = 34;
constexpr int JOY_Y = 35;
constexpr int JOY_BUTTON = 27;
constexpr int FORCE_PIN = 32;
constexpr int SERVO_PIN = 18;
constexpr bool HARDWARE_CONFIGURED = false; // Set true after checking wiring/limits.
constexpr int OPEN_US = 1200;
constexpr int CLOSED_US = 1800; // Must be calibrated to the actual linkage.
constexpr int FORCE_STOP_ADC = 2400; // Placeholder raw threshold, not newtons.
constexpr int FORCE_RELEASE_ADC = 2200;
constexpr int DEADBAND = 250;
constexpr int STEP_US = 3;

int centreX = 0;
int centreY = 0;
int servoUs = OPEN_US;
bool forceLimited = false;
uint32_t lastTick = 0;
uint32_t lastReport = 0;

bool writeServo(int pulseUs) {
  const uint32_t duty = uint32_t(pulseUs) * 65535UL / 20000UL;
  return ledcWrite(SERVO_PIN, duty);
}

void setup() {
  Serial.begin(115200);
  pinMode(JOY_BUTTON, INPUT_PULLUP);
  analogReadResolution(12);
  analogSetPinAttenuation(JOY_X, ADC_11db);
  analogSetPinAttenuation(JOY_Y, ADC_11db);
  analogSetPinAttenuation(FORCE_PIN, ADC_11db);
  // Keep joystick centred throughout startup calibration.
  for (int i = 0; i < 100; ++i) {
    centreX += analogRead(JOY_X);
    centreY += analogRead(JOY_Y);
    delay(5);
  }
  centreX /= 100;
  centreY /= 100;
  if (!HARDWARE_CONFIGURED) {
    Serial.println("Draft configuration: servo disabled; check wiring and limits.");
    return;
  }
  if (centreX < 500 || centreX > 3500 || centreY < 500 || centreY > 3500) {
    Serial.println("Joystick calibration failed; servo disabled.");
    while (true) delay(1000);
  }
  if (!ledcAttach(SERVO_PIN, 50, 16) || !writeServo(servoUs)) {
    Serial.println("Servo PWM initialization failed.");
    ledcDetach(SERVO_PIN);
    while (true) delay(1000);
  }
}

void loop() {
  const uint32_t now = millis();
  if (now - lastTick < 20) return;
  lastTick = now;
  const int x = analogRead(JOY_X) - centreX;
  const int y = analogRead(JOY_Y) - centreY;
  const int force = analogRead(FORCE_PIN);
  if (force >= FORCE_STOP_ADC) forceLimited = true;
  if (force <= FORCE_RELEASE_ADC) forceLimited = false;

  // Hold the joystick switch to enable motion. Y positive closes, negative opens.
  // Force threshold blocks further closing; opening remains available.
  if (HARDWARE_CONFIGURED && digitalRead(JOY_BUTTON) == LOW) {
    int nextUs = servoUs;
    if (y < -DEADBAND) nextUs -= STEP_US;
    if (y > DEADBAND && !forceLimited) nextUs += STEP_US;
    nextUs = constrain(nextUs, OPEN_US, CLOSED_US);
    if (nextUs != servoUs) {
      if (!writeServo(nextUs)) {
        ledcDetach(SERVO_PIN);
        Serial.println("PWM write failed; servo output disabled.");
        while (true) delay(1000);
      }
      servoUs = nextUs;
    }
  }
  if (now - lastReport >= 250) {
    lastReport = now;
    Serial.printf("x=%d y=%d force_adc=%d pulse_us=%d limited=%d\n",
                  x, y, force, servoUs, forceLimited);
  }
}
