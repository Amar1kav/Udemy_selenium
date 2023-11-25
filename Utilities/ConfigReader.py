from configparser import ConfigParser


class ReadConfig:
    config = ConfigParser()
    config.read(filenames="..//Configurations//config.ini")

    def get_locators(self, locator, value):
        values = self.config.get(locator, value)
        return values
