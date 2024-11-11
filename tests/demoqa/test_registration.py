from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_add_content():
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(capabilities)
    options.page_load_strategy = "eager"
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.open('https://demoqa.com/automation-practice-form')
    browser.quit()