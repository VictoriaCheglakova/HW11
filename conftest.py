from xml.dom.xmlbuilder import Options

import pytest
from requests import options
from selene import browser, Browser, Config
from selenium import webdriver



@pytest.fixture(scope='function')
def setup_browser(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-notifications')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-infobars')
    # options.add_argument('--enable-automation')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-setuid-sandbox')
    # browser.config.driver_options = options
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
        # desired_capabilities=selenoid_capabilities)
    # browser.open('https://demoqa.com/automation-practice-form')
    browser = Browser(Config(driver))
    yield browser
    browser.quit()