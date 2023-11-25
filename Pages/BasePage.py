from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.ConfigReader import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

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

        log.logger.info("Finding the element locator"+str(value))
    def click(self, locator, value):
        self.wait = WebDriverWait(self.driver, 10)
        if str(value).endswith("_XPATH"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, ReadConfig().get_locators(locator, value)))).click()
            # self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_CSS"):
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ReadConfig().get_locators(locator, value)))).click()

        if str(value).endswith("_ID"):
            self.wait.until(EC.element_to_be_clickable((By.ID, ReadConfig().get_locators(locator, value)))).click()

        if str(value).endswith("_NAME"):
            self.wait.until(EC.element_to_be_clickable((By.NAME, ReadConfig().get_locators(locator, value)))).click()
        log.logger.info("clicking the element locator" + str(value))
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
        log.logger.info("sendkeys the element locator" + str(value))
    def select_by_visible_text(self, locator, value, text):
        drop_down = self.find_element(locator, value)
        select = Select(drop_down)
        select.select_by_visible_text(text)
        log.logger.info("selecting  the element visible" + str(value)+ f"and value is {text}")
    def get_testUrl(self, locator, value):
        self.driver.get(ReadConfig().get_locators(locator, value))
        log.logger.info("Launching url")