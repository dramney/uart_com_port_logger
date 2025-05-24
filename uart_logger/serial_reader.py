import serial
from datetime import datetime
from storage import DataStorage
from logger import Logger

class SerialReader:
    def __init__(self, port: str, baudrate: int, storage: DataStorage, logger: Logger):
        self.port = port
        self.baudrate = baudrate
        self.storage = storage
        self.logger = logger

    def listen(self):
        try:
            with serial.Serial(self.port, self.baudrate, timeout=1) as ser:
                self.logger.log(f"Listening on {self.port} at {self.baudrate} baud...")
                while True:
                    line = ser.readline().decode(errors='ignore').strip()
                    if line:
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        self.logger.log(line)
                        self.storage.save(timestamp, line)
        except serial.SerialException as e:
            self.logger.error(f"Serial error: {e}")
        except KeyboardInterrupt:
            self.logger.log("Stopped by user.")
