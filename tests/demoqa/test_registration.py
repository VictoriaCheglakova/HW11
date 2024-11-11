from selene import browser


def test_add_content(open_browser):
    browser.open('https://demoqa.com/automation-practice-form')