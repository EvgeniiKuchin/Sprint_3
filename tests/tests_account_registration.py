from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import random


class Test_account_rg:
    def test_registration_new_user_data_all_correct(self, browser):

        browser.get("https://stellarburgers.nomoreparties.site/register")
        name_field = browser.find_element(By.XPATH, Locators.ELELENT_NAME_REGISTRATION)
        rando_name = "Test_Use" + str(random.randint(1, 99999))
        rando_pass = random.randint(100000, 999999)
        rando_email = "evgnii" + str(random.randint(1, 9999)) + "@ya.ru"
        name_field.send_keys(rando_name)
        email_field = browser.find_element(By.XPATH, Locators.ELELENT_EMAIL_REGISTRATION)
        email_field.send_keys(rando_email)
        password_field = browser.find_element(By.XPATH, Locators.ELELENT_PASSWORD_REGISTTATION)
        password_field.send_keys(rando_pass)
        browser.find_element(By.XPATH, Locators.BUTTON_REGISTER).click()

        browser.get("https://stellarburgers.nomoreparties.site/login")
        email_field = browser.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys(rando_email)
        password_field = browser.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys(rando_pass)
        browser.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()

        browser.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        assert browser.find_element(By.XPATH, Locators.TEXT_PROFILE).text == 'Профиль'

    def test_login_verification_successfully(self, browser):

        browser.get("https://stellarburgers.nomoreparties.site/login")
        email_field = browser.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys("12345@ya.ru")
        password_field = browser.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys("123456")
        browser.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()
        browser.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        assert browser.find_element(By.XPATH, Locators.TEXT_PROFILE).text == 'Профиль'


    def test_registration_new_user_incorrect_password(self, browser):

        browser.get("https://stellarburgers.nomoreparties.site/register")
        # Заполнить поля для регистрации
        name_field = browser.find_element(By.XPATH,Locators.ELELENT_NAME_REGISTRATION)
        name_field.send_keys("Test_User")
        email_field = browser.find_element(By.XPATH,Locators.ELELENT_EMAIL_REGISTRATION)
        email_field.send_keys("123@ya.ru")
        password_field = browser.find_element(By.XPATH,Locators.ELELENT_PASSWORD_REGISTTATION)
        password_field.send_keys("12345")
        browser.find_element(By.XPATH,Locators.BUTTON_REGISTER).click()
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_INCORRECT_PASSWORD)))

        assert browser.find_element(By.XPATH, Locators.TEXT_INCORRECT_PASSWORD).text == 'Некорректный пароль'



    def test_logout(self, browser):

        browser.get("https://stellarburgers.nomoreparties.site/login")
        email_field = browser.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys("12345@ya.ru")
        password_field = browser.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys("123456")
        browser.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()

        browser.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.BUTTON_LOG_OUT)))
        browser.find_element(By.XPATH, Locators.BUTTON_LOG_OUT).click()
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_ENTRANCE)))

        assert browser.find_element(By.XPATH, Locators.TEXT_ENTRANCE).text == 'Вход'



