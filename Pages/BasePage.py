from selenium import webdriver
from selenium.webdriver import ActionChains
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
            log.logger.info("Finding the  xpath")
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_CSS"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_ID"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_NAME"):
            return self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        log.logger.info("Finding the element locator" + str(value))

    def click_ele(self, locator, value):
        self.wait = WebDriverWait(self.driver, 10)
        if str(value).endswith("_XPATH"):
            log.logger.info("click  element XPATH locator" + str(value))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, ReadConfig().get_locators(locator, value)))).click()
            # self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value))

        if str(value).endswith("_CSS"):
            self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ReadConfig().get_locators(locator, value)))).click()

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
            self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)

        if str(value).endswith("_ID"):
            self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)

        if str(value).endswith("_NAME"):
            self.driver.find_element(By.XPATH, ReadConfig().get_locators(locator, value)).send_keys(text)
        log.logger.info("sendkeys the element locator" + str(value))

    def select_by_visible_text(self, locator, value, text):
        drop_down = self.find_element(locator, value)
        select = Select(drop_down)
        select.select_by_visible_text(text)
        log.logger.info("selecting  the element visible" + str(value) + f"and value is {text}")

    def get_testUrl(self, locator, value):
        self.driver.get(ReadConfig().get_locators(locator, value))
        log.logger.info("Launching url")

    def moveTo(self, value):
        log.logger.info(f"Finding the element locator move to xpath {value}")
        element = None
        if str(value).endswith("_XPATH"):
            log.logger.info("Finding the element locator move to xpath")
            element = self.driver.find_element(By.XPATH, ReadConfig().get_locators("locators", value))

        if str(value).endswith("_CSS"):
            element = self.driver.find_element(By.XPATH, ReadConfig().get_locators("locators", value))

        if str(value).endswith("_ID"):
            element = self.driver.find_element(By.XPATH, ReadConfig().get_locators("locators", value))

        if str(value).endswith("_NAME"):
            element = self.driver.find_element(By.XPATH, ReadConfig().get_locators("locators", value))
        log.logger.info("Finding the element locator" + str(element))
        action = ActionChains(self.driver)

        action.move_to_element(element).perform()
        log.logger.info("Finding the element locator" + str(value))

    def handle_alerts(self):
        try:
            alert = self.driver.switch_to.alert()
            log.logger.info(f"Alert is oject is present hence Exception occured is : {alert}")
            alert.accept()
        except Exception as err:
            log.logger.info(f"Alert is not present hence Exception occured is : {err}" )
