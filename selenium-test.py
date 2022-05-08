from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com')

    def go_to_login_page(self):
        return LoginPage(self.browser)


browser = webdriver.Firefox(executable_path='/Users/akin/Desktop/geckodriver')
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("akinyolci", "Nika")

browser.close()


def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("akinyolci", "Nika")

    errors = browser.find_element(By.CSS_SELECTOR, '#error_message')
    assert len(errors) == 0


test_login_page(browser)
