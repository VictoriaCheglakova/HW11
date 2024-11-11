import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    # browser.config.base_url = "https://demoqa.com/automation-practice-form/"
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

    yield browser
    browser.quit()