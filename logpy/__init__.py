"""
Author: Avinash Kanumuru
Contact: avinash.eee@gmail.com
Date: 2024-07-17
Version: 1.0
Description: 
"""

import logging
from logging.handlers import RotatingFileHandler

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(asctime)s] [%(levelname)8s] [%(name)s - %(filename)s:%(lineno)d] - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def __init__(self, use_color=True):
        super().__init__()
        self.use_color = use_color

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        if self.use_color:
            formatter = logging.Formatter(log_fmt)
        else:
            formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] [%(name)s - %(filename)s:%(lineno)d] - %(message)s")
        return formatter.format(record)

class CustomLogger(logging.Logger):
    def __init__(self, name='UtilsLogger', level=logging.INFO):
        super().__init__(name, level)     
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)
        # ch_formatter = logging.Formatter(CustomFormatter())
        ch.setFormatter(CustomFormatter())
        self.addHandler(ch)
        
        # File handler
        fh = RotatingFileHandler('app.log', maxBytes=1024*1024*5, backupCount=5)
        fh.setLevel(level)
        # fh_formatter = logging.Formatter(format)
        fh.setFormatter(CustomFormatter(use_color=False))
        self.addHandler(fh)

    def getLogger(self, name='UtilsLogger'):
        if name:
            return super().getLogger(name)
        else:
            return self
        
logging.setLoggerClass(CustomLogger)