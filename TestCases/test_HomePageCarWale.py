import time
import pytest
from TestCases.BaseTestPage import BaseTestPage
from Utilities.ConfigReader import ReadConfig
import logging
from Utilities.LogUtil import Logger
from Pages.HomePage_CarWale import HomePage_CarWale

log = Logger(__name__, logging.INFO)


class Test_HomePageCarWale(BaseTestPage):
    read_data = ReadConfig()

    @pytest.mark.test
    def test_new_Car(self):
        log.logger.info("entering the test_new car testcase")
        homepage_car = HomePage_CarWale(self.driver)
        homepage_car.get_testUrl("basic_info", "testurl")
        homepage_car.gotofindNewCar()
        time.sleep(5)
        self.driver.quit()