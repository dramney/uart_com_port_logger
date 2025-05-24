import json
import csv
import os

class DataStorage:
    def __init__(self, base_filename: str):
        self.json_path = f"{base_filename}.json"
        self.csv_path = f"{base_filename}.csv"
        self._init_csv()

    def _init_csv(self):
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, "w", newline="", encoding="utf-8") as cf:
                writer = csv.writer(cf)
                writer.writerow(["timestamp", "message"])

    def save(self, timestamp: str, message: str):
        entry = {
            "timestamp": timestamp,
            "message": message
        }
        with open(self.json_path, "a", encoding="utf-8") as jf:
            jf.write(json.dumps(entry) + "\n")

        with open(self.csv_path, "a", newline="", encoding="utf-8") as cf:
            writer = csv.writer(cf)
            writer.writerow([timestamp, message])
