import time

import pytest

from TestCases.BaseTestPage import BaseTestPage
from Utilities.ConfigReader import ReadConfig
import logging
from Utilities.LogUtil import Logger
from Pages.NewCarHomePage import NewCarHomePage
from Pages.HomePage_CarWale import HomePage_CarWale
log = Logger(__name__, logging.INFO)


class Test_HomePageCarWale(BaseTestPage):
    read_data = ReadConfig()

    @pytest.mark.test1
    def test_go_verify_Car_Title(self):
        log.logger.info("entering the go to car title")
        homepage_car = HomePage_CarWale(self.driver)
        homepage_car.get_testUrl("basic_info", "testurl")
        homepage_car.gotofindNewCar()
        time.sleep(5)
        newcar = NewCarHomePage(self.driver)
        newcar.go_to_Maruthi()
        time.sleep(5)
        log.logger.info(f"driver title : {self.driver.title}")

        if self.driver.title == "Maruti Suzuki Car Price in India - Nexa Models 2023 - Reviews, Specs & Dealers - " \
                                "CarWale":
            log.logger.info("Maruthi title is verified")
            self.driver.back()

        newcar.go_to_Hyndai()
        time.sleep(5)
        if self.driver.title == "Hyundai Cars Price in India - Hyundai Models 2023 - Reviews, Specs & Dealers - CarWale":
            log.logger.info("Hyundai title is verified")
            self.driver.back()

        self.driver.quit()
        # if self.driver.title == "New Cars in India 2023 | New Car Information | Best New Cars - CarWale":
        #     log.logger.info("Home Page title is verified")
