# BNO055 Sensor Data Logger with Arduino and Python

This project reads real-time orientation data (X, Y, Z Euler angles) and calibration status from an Adafruit BNO055 9-DOF absolute orientation sensor using an Arduino. A Python script then reads this data from the serial port and logs it into a `bno_data.csv` file.

**Author:** Afeez

## Table of Contents
1.  Hardware Prerequisites
2.  Software Prerequisites
3.  Setup and Installation
    *   Arduino Setup
    *   Python Setup
4.  How to Run the Project
5.  Code Explanation
    *   Arduino Sketch
    *   Python Script (`log_bno.py`)
6.  Output Data Format

## Hardware Prerequisites

*   Arduino board (e.g., Arduino Uno, Nano, etc.)
*   Adafruit BNO055 Absolute Orientation Sensor
*   Breadboard and connecting wires

## Software Prerequisites

*   Arduino IDE
*   Python 3
*   `pyserial` Python library

## Setup and Installation

### Arduino Setup

1.  **Wiring:** Connect the BNO055 sensor to your Arduino using the I2C interface.
    *   `VIN` -> Arduino `5V`
    *   `GND` -> Arduino `GND`
    *   `SDA` -> Arduino `SDA` (A4 on Uno) // for Ardunio DEV R3 board pin 20
    *   `SCL` -> Arduino `SCL` (A5 on Uno) // for Ardunio DEV R3 board pin 21

2.  **Install Arduino Libraries:**
    *   Open the Arduino IDE.
    *   Go to **Sketch** -> **Include Library** -> **Manage Libraries...**.
    *   Search for and install the following libraries:
        *   `Adafruit Unified Sensor`
        *   `Adafruit BNO055`
    *   The `Wire.h` and `utility/imumaths.h` libraries are included with the Arduino IDE and the BNO055 library, respectively, so no separate installation is needed for them.
    
3.  **Load the Sketch:**
    *   Copy the provided C++ code into a new sketch in the Arduino IDE.
    *   **Important:** The BNO055 sensor can have an I2C address of `0x28` or `0x29`. The provided code uses `0x28`. If your sensor is not detected, you may need to change this line:
        ```cpp
        Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28, &Wire);
        ```
    *   Connect your Arduino to your computer, select the correct board and port from the **Tools** menu, and click the **Upload** button.

### Python Setup

1.  **Install `pyserial`:** This library is required to read data from the serial port. Open your terminal or PowerShell and run:
    ```sh
    pip install pyserial
    ```

2.  **Configure the Python Script (`log_bno.py`):**
    *   Open the `log_bno.py` file.
    *   Find your Arduino's port in the Arduino IDE under **Tools -> Port** (e.g., `COM8`, `/dev/ttyUSB0`).
    *   Update the `PORT` variable in the script with your port name:
        ```python
        # Replace COM8 with your Arduino's port.
        PORT = "COM8"
        ```

## How to Run the Project

1.  Ensure your Arduino with the BNO055 is connected to your computer and the sketch has been uploaded.
2.  Open a terminal or PowerShell.
3.  Navigate to the directory where you saved the `log_bno.py` file.
4.  Run the Python script:
    ```sh
    python log_bno.py
    ```
5.  The script will connect to the Arduino and start printing the sensor data to the console. It will also save the data to `bno_data.csv` in the same directory.
6.  To stop logging, press `Ctrl+C` in the terminal. The script will then close the serial port and the file safely.

## Code Explanation

### Arduino Sketch
The Arduino code initializes the BNO055 sensor and establishes serial communication. In the main `loop()`, it continuously fetches the Euler angles vector (`VECTOR_EULER`) and the calibration status of the system, gyroscope, accelerometer, and magnetometer. This data is then formatted and printed to the serial port. A small delay is added to control the sampling rate.

### Python Script (`log_bno.py`)
This script connects to the specified serial port (`PORT`) at the defined `BAUDRATE`. It opens `bno_data.csv` in write mode. In an infinite loop, it reads each line of data sent by the Arduino, decodes it from bytes to a UTF-8 string, and writes it to both the console and the CSV file. The `try...except` block ensures that if you interrupt the script (`Ctrl+C`) or an error occurs, the serial port is properly closed.

## Output Data Format

The `bno_data.csv` file will contain the raw output from the sensor, with each line representing a single reading. The format for the data lines is as follows:
```
 python log_bno.py
```

```
X: [euler_x] Y: [euler_y] Z: [euler_z]		CALIBRATION: Sys=[0-3] Gyro=[0-3] Accel=[0-3] Mag=[0-3]
```
*   **X, Y, Z:** These are the Euler angle outputs representing the orientation of the sensor.
*   **CALIBRATION:** These values indicate the calibration status for each component of the sensor, where `0` is uncalibrated and `3` is fully calibrated.