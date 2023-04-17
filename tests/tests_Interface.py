from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class Test_interface:
    def test_entrance_by_button_on_the_main(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        button_account_login = driver.find_element(By.XPATH, Locators.BUTTON_IN_ACCOUNT)
        button_account_login.click()
        email_field = driver.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys("12345@ya.ru")
        password_field = driver.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys("123456")
        password_field.submit()
        #driver.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()

        driver.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        assert driver.find_element(By.XPATH, Locators.TEXT_PROFILE).text == 'Профиль'
        driver.quit()

    def test_button_on_the_main_Personal_Are(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        button_on_the_main_Personal_Are = driver.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA)
        button_on_the_main_Personal_Are.click()
        email_field = driver.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys("12345@ya.ru")
        password_field = driver.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys("123456")
        driver.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()
        driver.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        assert driver.find_element(By.XPATH, Locators.TEXT_PROFILE).text == 'Профиль'
        driver.quit()

    def test_button_in_the_registration_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        button_in_the_registration_form = driver.find_element(By.XPATH, Locators.BUTTON_IN_ACCOUNT_FORM)
        button_in_the_registration_form.click()
        email_field = driver.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys("12345@ya.ru")
        password_field = driver.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys("123456")
        driver.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()
        driver.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        assert driver.find_element(By.XPATH, Locators.TEXT_PROFILE).text == 'Профиль'
        driver.quit()

    def test_button_password_recovery_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        button_password_recovery_form = driver.find_element(By.XPATH, Locators.BUTTON_IN_ACCOUNT_FORM)
        button_password_recovery_form.click()
        email_field = driver.find_element(By.XPATH, Locators.ELEMENT_IN_MAIL)
        email_field.send_keys("12345@ya.ru")
        password_field = driver.find_element(By.XPATH, Locators.ELELENT_IN_PASS)
        password_field.send_keys("123456")
        driver.find_element(By.XPATH, Locators.BUTTON_SING_IN).click()
        driver.find_element(By.XPATH, Locators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.TEXT_PROFILE)))
        assert driver.find_element(By.XPATH, Locators.TEXT_PROFILE).text == 'Профиль'
        driver.quit()
    def test_Button_to_enter_Personal_Account(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        button_password_recovery_form = driver.find_element(By.XPATH, Locators.BUTTON_IN_ACCOUNT_FORM)
        button_password_recovery_form.click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
    def test_button_to_constructor(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        button_to_constructor = driver.find_element(By.XPATH, Locators.BUTTON_CONSTRUCTOR)
        button_to_constructor.click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
    def test_click_logo(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        button_to_constructor = driver.find_element(By.XPATH, Locators.BUTTON_MAIN_LOGO)
        button_to_constructor.click()
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_button_sauces(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.BUTTON_SOUS)))

        driver.find_element(By.XPATH, "BUTTON_SOUS").click()
        assert driver.find_element(By.XPATH, Locators.TEXT_SOUS).text == 'Соусы'
        driver.quit()
    def test_button_fillings(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.FILLINGS)))
        driver.find_element(By.XPATH, Locators.FILLINGS).click()
        assert driver.find_element(By.XPATH, Locators.TEXT_FILLINGS).text == 'Начинки'
        driver.quit()

    def test_button_fillings(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.BAGEL)))
        driver.find_element(By.XPATH, Locators.BAGEL).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.BAGEL)))
        assert driver.find_element(By.XPATH, Locators.TEXT_BAGEL).text == 'Булки'
        driver.quit()