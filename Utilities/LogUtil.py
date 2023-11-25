import logging
import time

class Logger:
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter("%(asctime)s- %(filename)s:[%(lineno)s] - [%(levelname)s]- %(message)s")
        cur_time = time.strftime("%Y-%m-%d")
        self.logFileName = r'..\\Logs\\log ' + cur_time + '.txt'
        # "a" append logs in same file , "W" to genertate new logs deleting old logs
        fh = logging.FileHandler(self.logFileName, mode="w")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)