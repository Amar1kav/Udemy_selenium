from Pages.BasePage import BasePage


class NewCarHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_Hyndai(self):
        self.click_ele("locators", "hyndai_XPATH")

    def go_to_Maruthi(self):
        self.click_ele("locators", "maruthi_XPATH")

    def go_to_Tata(self):
        self.click_ele("locators", "tata_XPATH")
