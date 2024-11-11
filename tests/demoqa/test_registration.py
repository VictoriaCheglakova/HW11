from selene import browser


def test_add_content(setup_browser):
    browser.open('https://demoqa.com/automation-practice-form')