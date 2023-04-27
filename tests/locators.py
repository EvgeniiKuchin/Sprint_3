

class Locators:
    BUTTON_IN_ACCOUNT = "//button[contains(text(), 'Войти в аккаунт') and contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]"# Большая кнопка войти в аккаунт на главной транице
    ELEMENT_IN_MAIL = "//input[@class='text input__textfield text_type_main-default' and @name='name']" # Строка ввода емэил
    ELELENT_IN_PASS = "//input[@class='text input__textfield text_type_main-default' and @type='password']"# Строка ввода пароля
    BUTTON_SING_IN = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']" # Кнопка войти
    BUTTON_PERSONAL_AREA = "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']" # Кнопка личный кабинет
    TEXT_PROFILE = "//a[contains(text(),'Профиль')]" # Текст на странице "Профиль"
    BUTTON_IN_ACCOUNT_FORM = "//a[contains(text(),'Войти')]" # Маленькая кнопка Войти на форме регистрации
    BUTTON_CONSTRUCTOR = "//p[contains(text(),'Конструктор')]" #
    BUTTON_MAIN_LOGO = "//header/nav[1]/div[1]/a[1]/*[1]" #
    BUTTON_SOUS = "//span[contains(text(),'Соусы')]" # Кнопка соусы
    TEXT_SOUS = "//h2[contains(text(),'Соусы')]" # Текст соусы
    FILLINGS = "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[3]/span[1]" # Кнопка начинки
    TEXT_FILLINGS = "//h2[contains(text(),'Начинки')]" # Текст начинки
    BAGEL = "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[1]/span[1]" # Кнопка булки
    TEXT_BAGEL = "//h2[contains(text(),'Булки')]" # Текст булки
    ELELENT_NAME_REGISTRATION = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]"
    ELELENT_EMAIL_REGISTRATION = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]"
    ELELENT_PASSWORD_REGISTTATION = "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]"
    BUTTON_REGISTER = "//button[contains(text(),'Зарегистрироваться')]"
    TEXT_INCORRECT_PASSWORD = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]"
    BUTTON_LOG_OUT = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/nav[1]/ul[1]/li[3]/button[1]"
    TEXT_ENTRANCE = "//h2[contains(text(),'Вход')]"