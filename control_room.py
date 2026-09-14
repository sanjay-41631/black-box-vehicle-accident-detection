import os
import serial
from datetime import datetime

SERIAL_PORT = os.getenv("CONTROL_ROOM_PORT", "COM5")
BAUD_RATE = int(os.getenv("CONTROL_ROOM_BAUD", "9600"))
LOG_FILE = os.getenv("CONTROL_ROOM_LOG", "accident_log.txt")

ACCIDENT_KEYWORDS = (
    "ACCIDENT DETECTED",
    "Ultrasonic Crash Detected",
    "IR Impact Detected",
)

def is_accident_event(line):
    return any(keyword.lower() in line.lower() for keyword in ACCIDENT_KEYWORDS)

def main():
    print("==== CONTROL ROOM MONITOR STARTED ====")
    print(f"Serial port: {SERIAL_PORT} | Baud rate: {BAUD_RATE}")
    print("Monitoring Arduino/ESP32 data...")

    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()

                if not line:
                    continue

                print(line)

                if is_accident_event(line):
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    with open(LOG_FILE, "a", encoding="utf-8") as log:
                        log.write(f"{timestamp} - {line}\n")

                    print("\n===== EMERGENCY ALERT =====")
                    print(f"{timestamp} - {line}")
                    print("============================\n")

    except serial.SerialException as exc:
        print(f"Serial connection error: {exc}")
        print("Check the COM port, USB cable and baud rate.")
    except KeyboardInterrupt:
        print("\nControl Room Monitor Stopped")

if __name__ == "__main__":
    main()
