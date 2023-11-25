import time

import pytest

from TestCases.BaseTestPage import BaseTestPage
from Utilities import ReadExcel
from Pages.Registration_Page import RegistrationPage
from Utilities.ConfigReader import ReadConfig


class Test_Signup(BaseTestPage):
    read_data = ReadConfig()

    @pytest.mark.parametrize("name, phonenum, email, country, city, username, password", ReadExcel.getData())
    def test_do_signup(self, setup, name, phonenum, email, country, city, username, password):
        self.driver.implicitly_wait(10)
        reg = RegistrationPage(self.driver)
        reg.get_testUrl("basic_info", "testurl")
        reg.fill_form(name, phonenum, email, city, username, password)
        reg.click_ele("button_submit_XPATH")
        alert_txt = reg.find_element("locators", "alert_XPATH")
        if alert_txt.text == "This is just a dummy form, you just clicked SUBMIT BUTTON":
            print("Alert is found hence ppassed")
        else:
            AssertionError("alert is not found")
