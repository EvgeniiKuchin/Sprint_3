

class Locators:
    BUTTON_IN_ACCOUNT = "//button[contains(text(), 'Войти в аккаунт') and contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]"# Большая кнопка войти в аккаунт на главной транице
    ELEMENT_IN_MAIL = "//input[@class='text input__textfield text_type_main-default' and @name='name']" # Строка ввода емэил
    ELELENT_IN_PASS = "//input[@class='text input__textfield text_type_main-default' and @type='password']"# Строка ввода пароля
    BUTTON_SING_IN = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']" # Кнопка войти
    BUTTON_PERSONAL_AREA = "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']" # Кнопка личный кабинет
    TEXT_PROFILE = "//a[contains(text(),'Профиль')]" # Текст на странице "Профиль"
    BUTTON_IN_ACCOUNT_FORM = "//a[contains(text(),'Войти')]" # Маленькая кнопка Войти на форме регистрации
    BUTTON_CONSTRUCTOR = "//p[contains(text(),'Конструктор')]" #
    BUTTON_MAIN_LOGO = "//div[@class='AppHeader_header__logo__2D0X2']"
    BUTTON_SOUS = "//span[@class='text text_type_main-default' and text()='Соусы']" # Кнопка соусы
    TEXT_SOUS = "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']" # Текст соусы
    FILLINGS = "//span[@class='text text_type_main-default' and text()='Начинки']" # Кнопка начинки
    TEXT_FILLINGS = "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']" # Текст начинки
    BAGEL = "//span[@class='text text_type_main-default' and text()='Булки']"
    TEXT_BAGEL = "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']" # Текст булки
    ELELENT_NAME_REGISTRATION = "//label[text()='Имя']/following-sibling::input"
    ELELENT_EMAIL_REGISTRATION = "//label[text()='Email']/following-sibling::input"
    ELELENT_PASSWORD_REGISTTATION = "//label[text()='Пароль']/following-sibling::input"
    BUTTON_REGISTER = "//button[contains(text(),'Зарегистрироваться')]"
    TEXT_INCORRECT_PASSWORD = "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']"
    BUTTON_LOG_OUT = "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']"
    TEXT_ENTRANCE = "//h2[text()='Вход']"
