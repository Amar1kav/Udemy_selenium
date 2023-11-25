import time

import pytest

from TestCases.BaseTestPage import BaseTestPage
from Utilities import ReadExcel
from Pages.Registration_Page import RegistrationPage
from Utilities.ConfigReader import ReadConfig
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

class Test_Signup(BaseTestPage):
    read_data = ReadConfig()

    @pytest.mark.parametrize("name, phonenum, email, country, city, username, password", ReadExcel.getData())
    def test_do_signup(self, setup, name, phonenum, email, country, city, username, password):
        log.logger.info("entering the test_do_singup")
        self.driver.implicitly_wait(10)
        reg = RegistrationPage(self.driver)
        reg.fill_form(name, phonenum, email, city, username, password)
        reg.click_ele("button_submit_XPATH")
        alert_txt = reg.find_element("locators", "alert_XPATH")
        if alert_txt.text == "This is just a dummy form, you just clicked SUBMIT BUTTON":
            log.logger.info("Successfullu singup")
        else:
            AssertionError("alert is not found")
