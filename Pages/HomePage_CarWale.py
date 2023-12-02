from Pages.BasePage import BasePage

class HomePage_CarWale(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gotofindNewCar(self):
        self.moveTo("newCar_XPATH")
        self.click_ele("locators", "findNewCar_XPATH")