from Pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, phoneNumber, email, city, username, password):
        print(name, phoneNumber, email, city, username, password)
        self.get_testUrl("basic_info", "testurl")
        self.send_keys("locators", "inputText_name_XPATH", name)
        self.send_keys("locators", "inputText_phone_XPATH", phoneNumber)
        self.send_keys("locators", "inputText_email_XPATH", email)
        self.send_keys("locators", "inputText_city_XPATH", city)
        self.select_by_visible_text("locators", "dropdown_XPATH", "Iceland")
        self.send_keys("locators", "inputText_username_XPATH", username)
        self.send_keys("locators", "inputText_password_XPATH", password)

    def click_ele(self, value):
        self.click("locators", value)
