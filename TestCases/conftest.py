from selenium import webdriver
import pytest

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request):
    from selenium.webdriver.chrome.options import Options
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    serv = Service(ChromeDriverManager().install())
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=serv, options=option)
    request.cls.driver = driver
    # if request.param == "firefox":
    #     serv = Service(GeckoDriverManager().install())
    #     driver = webdriver.Firefox(service=serv)
    return driver
