from configparser import ConfigParser
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

class ReadConfig:
    log.logger.info("Reading config")
    config = ConfigParser()
    config.read(filenames=r".//Configurations//config.ini")
    log.logger.info(f"config : {config}")
    def get_locators(self, locator, value):
        values = self.config.get(locator, value)
        return values
