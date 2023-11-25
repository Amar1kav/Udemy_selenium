from selenium import webdriver
import pytest

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request):
    from selenium.webdriver.chrome.options import Options
    serv = Service(ChromeDriverManager().install())
    opt = Options().add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=serv, options=opt)
    request.cls.driver = driver
    # if request.param == "firefox":
    #     serv = Service(GeckoDriverManager().install())
    #     driver = webdriver.Firefox(service=serv)
    return driver
