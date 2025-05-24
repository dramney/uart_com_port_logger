import argparse
from datetime import datetime
from logger import Logger
from serial_reader import SerialReader
from storage import DataStorage

def main():
    parser = argparse.ArgumentParser(description="UART Serial Logger")
    parser.add_argument('--port', required=True, help='COM port (e.g. COM3 or /dev/ttyUSB0)')
    parser.add_argument('--baudrate', type=int, default=9600, help='Baud rate (default: 9600)')
    args = parser.parse_args()

    base_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    logger = Logger(f"{base_filename}.txt")
    storage = DataStorage(base_filename)
    reader = SerialReader(args.port, args.baudrate, storage, logger)
    reader.listen()

if __name__ == "__main__":
    main()
