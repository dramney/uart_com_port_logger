import serial
import argparse
import logging
from datetime import datetime
import os
import json
import csv


def setup_logger(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def process_line(line, timestamp, json_path, csv_path):
    entry = {
        "timestamp": timestamp,
        "message": line
    }

    with open(json_path, "a", encoding="utf-8") as jf:
        jf.write(json.dumps(entry) + "\n")

    with open(csv_path, "a", newline="", encoding="utf-8") as cf:
        writer = csv.writer(cf)
        writer.writerow([timestamp, line])


def read_serial(port, baudrate, base_filename):
    json_path = f"{base_filename}.json"
    csv_path = f"{base_filename}.csv"

    if not os.path.exists(csv_path):
        with open(csv_path, "w", newline="", encoding="utf-8") as cf:
            writer = csv.writer(cf)
            writer.writerow(["timestamp", "message"])

    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            logging.info(f"Listening on {port} at {baudrate} baud...")
            while True:
                line = ser.readline().decode(errors='ignore').strip()
                if line:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    logging.info(line)
                    process_line(line, timestamp, json_path, csv_path)
    except serial.SerialException as e:
        logging.error(f"Serial error: {e}")
    except KeyboardInterrupt:
        logging.info("Stopped by user.")


def main():
    parser = argparse.ArgumentParser(description="UART Serial Logger")
    parser.add_argument('--port', required=True, help='COM port (e.g. COM3 or /dev/ttyUSB0)')
    parser.add_argument('--baudrate', type=int, default=9600, help='Baud rate (default: 9600)')
    args = parser.parse_args()

    base_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    setup_logger(f"{base_filename}.txt")

    read_serial(args.port, args.baudrate, base_filename)


if __name__ == "__main__":
    main()
