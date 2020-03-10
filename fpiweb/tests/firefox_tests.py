from selenium.webdriver import Firefox

if __name__ == '__main__':
    driver = Firefox(executable_path='../../geckodriver')
    driver.get('https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode')
