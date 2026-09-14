import os
import tkinter as tk
from tkinter import messagebox
import serial

PORT = os.getenv("BLACKBOX_PORT", "COM6")
BAUD = int(os.getenv("BLACKBOX_BAUD", "115200"))

def show_alert(data):
    root = tk.Tk()
    root.withdraw()

    message = (
        "🚨 ACCIDENT DETECTED 🚨\n\n"
        f"Driver: {data.get('DRIVER_NAME', '-')}\n"
        f"Age: {data.get('AGE', '-')}\n"
        f"Blood Group: {data.get('BLOOD_GROUP', '-')}\n"
        f"Emergency Contact: {data.get('EMERGENCY_CONTACT', '-')}\n"
        f"Reason: {data.get('REASON', '-')}\n\n"
        f"Latitude: {data.get('LAT', '-')}\n"
        f"Longitude: {data.get('LON', '-')}\n"
        f"GPS Time: {data.get('GPS_TIME', '-')}\n\n"
        f"Distance: {data.get('DISTANCE_CM', '-')} cm\n"
        f"Acceleration: {data.get('ACC_MAG', '-')}\n"
        f"Pitch: {data.get('PITCH', '-')}\n"
        f"Roll: {data.get('ROLL', '-')}"
    )

    messagebox.showerror("BLACK BOX EMERGENCY ALERT", message)
    root.destroy()

def main():
    print("🚨 BLACK BOX MONITOR STARTED 🚨")
    print(f"Serial port: {PORT} | Baud rate: {BAUD}")

    try:
        with serial.Serial(PORT, BAUD, timeout=1) as ser:
            collecting = False
            data = {}

            while True:
                line = ser.readline().decode(errors="ignore").strip()

                if not line:
                    continue

                print(line)

                if line == "ACCIDENT_START":
                    collecting = True
                    data = {}
                    continue

                if line == "ACCIDENT_END":
                    if collecting:
                        show_alert(data)
                    collecting = False
                    continue

                if collecting and "=" in line:
                    key, value = line.split("=", 1)
                    data[key.strip()] = value.strip()

    except serial.SerialException as exc:
        print(f"Serial connection error: {exc}")
        print("Check the COM port, USB cable and baud rate.")

if __name__ == "__main__":
    main()
