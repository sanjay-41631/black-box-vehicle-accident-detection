# 🚗 BLACK BOX – Vehicle Accident Detection & Emergency Alert System

A Python-based control-room and emergency-alert interface for a **smart vehicle black box** prototype.

The system receives accident information from a microcontroller over serial communication, records accident events, and displays an emergency alert containing sensor, driver, and GPS information.

> **Project type:** Embedded Systems + IoT + Safety Automation  
> **Status:** Prototype / Academic Project

## ✨ Features

- 🚨 Accident detection event handling
- 📡 Serial communication with Arduino/ESP32
- 🧭 GPS latitude, longitude and GPS time capture
- 📐 Acceleration, pitch and roll monitoring
- 📏 Ultrasonic crash-distance information
- 🖥️ Desktop emergency alert using Tkinter
- 🏢 Control-room monitoring
- 📝 Automatic accident event logging
- 🔐 Configuration through environment variables instead of hard-coded secrets

## 🧠 System Architecture

```text
┌───────────────────────┐
│ Sensors / GPS / IMU   │
│ Ultrasonic + MPU6050  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Arduino / ESP32       │
│ Accident Detection    │
└───────────┬───────────┘
            │ USB Serial
            ▼
┌───────────────────────┐
│ Python Control Room   │
│ Serial Monitor        │
└───────────┬───────────┘
            │
       Accident Event
            │
      ┌─────┴─────┐
      ▼           ▼
┌───────────┐ ┌────────────┐
│ Event Log │ │ GUI Alert  │
└───────────┘ └────────────┘
```

## 🛠️ Hardware

Typical prototype components:

- Arduino / ESP32
- MPU6050 accelerometer + gyroscope
- GPS NEO-6M
- HC-SR04 ultrasonic sensor
- IR impact sensor (optional)
- OLED display (optional)
- Buzzer / LED (optional)

## 💻 Software

- Python 3.10+
- PySerial
- Tkinter
- Arduino IDE / ESP32 Arduino Core

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/black-box-vehicle-accident-detection.git
cd black-box-vehicle-accident-detection
```

Install the Python dependency:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Set the serial port before running.

### Windows PowerShell

```powershell
$env:BLACKBOX_PORT="COM6"
$env:BLACKBOX_BAUD="115200"
python blackbox_alert.py
```

For the control-room monitor:

```powershell
$env:CONTROL_ROOM_PORT="COM5"
$env:CONTROL_ROOM_BAUD="9600"
python control_room.py
```

The default values are provided for convenience, but using environment variables makes the project easier to move between computers.

## 📡 Serial Data Format

The Python alert program expects an event such as:

```text
ACCIDENT_START
DRIVER_NAME=Demo Driver
AGE=21
BLOOD_GROUP=O+
EMERGENCY_CONTACT=XXXXXXXXXX
REASON=Ultrasonic Crash Detected
LAT=9.9312
LON=76.2673
GPS_TIME=12:30:45
DISTANCE_CM=8
ACC_MAG=3.42
PITCH=12.5
ROLL=-4.2
ACCIDENT_END
```

**Use dummy data when publishing examples. Do not commit real personal information.**

## 📁 Project Structure

```text
.
├── blackbox_alert.py      # Desktop emergency alert monitor
├── control_room.py        # Serial control-room logger
├── accident_log.txt       # Example/test event log
├── requirements.txt       # Python dependency list
├── .gitignore             # Files that should not be committed
├── .env.example           # Configuration template
└── README.md              # Project documentation
```

## 🔐 Security

Never upload:

- Telegram bot tokens
- API keys
- passwords
- real emergency-contact numbers
- real driver medical information
- private GPS/location data

If a secret has already been pushed to GitHub, **revoke/rotate it immediately**. Deleting the file in a later commit does not make an exposed secret safe.

## 🔮 Future Improvements

- Telegram/SMS emergency notification
- Automatic nearest-hospital lookup
- Cloud accident database
- Web dashboard for the control room
- ESP32 Wi-Fi / MQTT communication
- Crash severity classification using sensor data
- Secure authentication
- Real-time map visualization
- Data analytics and accident-pattern detection

## 👨‍💻 Author

**Sanjay S.**  
B.Tech Robotics & Automation Engineering Student

Interested in Embedded Systems, IoT, Robotics, ROS, Computer Vision and Automation.
