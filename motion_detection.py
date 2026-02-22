import RPi.GPIO as GPIO
import time

# -----------------------------
# GPIO Configuration
# -----------------------------
PIR_PIN = 17      # PIR Sensor
LED_PIN = 22      # Maker pHAT LED
BUZZER_PIN = 27   # Maker pHAT Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Ensure outputs start OFF
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.output(BUZZER_PIN, GPIO.LOW)

print("Initializing PIR Sensor...")
time.sleep(5)  # PIR needs warm-up time
print("System Ready!")

try:
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            print("Motion Detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)

            time.sleep(1)  # Active for 1 second

        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")