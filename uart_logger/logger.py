import logging


class Logger:
    def __init__(self, log_file: str):
        self._setup_logger(log_file)
        
    def _setup_logger(self, log_file: str):
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(message)s',
            datefmt='%H:%M:%S',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

    def log(self, message: str):
        logging.info(message)

    def error(self, message: str):
        logging.error(message)
