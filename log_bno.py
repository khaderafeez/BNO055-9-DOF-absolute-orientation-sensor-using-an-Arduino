import serial
import time

# Replace COM3 with your Arduino's port.
# You can find the correct port in Arduino IDE under Tools -> Port
PORT = "COM8"
BAUDRATE = 115200

# Generate a unique filename with a timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILE = f"bno_data_{timestamp}.csv"

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Connected to {PORT} at {BAUDRATE} baud")
    time.sleep(2)  # Give Arduino time to reset

    with open(OUTPUT_FILE, 'w', newline='') as file:
        print(f"Logging data to {OUTPUT_FILE}... Press Ctrl+C to stop.")
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print(line)
                file.write(line + '\n')
except KeyboardInterrupt:
    print("\nLogging stopped by user.")
except Exception as e:
    print(f"Error: {e}")
finally:
    ser.close()
    print("Serial port closed.")
