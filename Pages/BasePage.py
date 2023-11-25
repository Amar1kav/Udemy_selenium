from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.ConfigReader import ReadConfig


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, value):
        if str(value).endswith("_XPATH"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_CSS"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_ID"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_NAME"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

    def click(self, locator, value):
        if str(value).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).click()

        if str(value).endswith("_CSS"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).click()

        if str(value).endswith("_ID"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).click()

        if str(value).endswith("_NAME"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).click()

    def send_keys(self, locator, value, text):
        if str(value).endswith("_XPATH"):
            print("xpath gone")
            self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)

        if str(value).endswith("_CSS"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)

        if str(value).endswith("_ID"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)

        if str(value).endswith("_NAME"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)

    def select_by_visible_text(self, locator, value , text):
        drop_down = self.find_element(locator, value)
        select = Select(drop_down)
        select.select_by_visible_text(text)

    def get_testUrl(self, locator, value):
        self.driver.get(ReadConfig().get_locators(locator, value))