from selene import browser, have, be
import allure

class AuthMOEX:

    @allure.step("Открыть сайт Московской биржи")
    def open(self):
        browser.open("/")

    @allure.step("Нажать кнопку 'Войти'")
    def press_tab_enter(self):
        browser.element("#header-user-profile").click()

    @allure.step("Ввести электронную почту")
    def fill_email(self, value):
        browser.element("#email").type(value)

    @allure.step("Ввести пароль")
    def fill_password(self, value):
        browser.element("#password").type(value)

    @allure.step("Нажать кнопку 'Войти'")
    def press_tab_login(self):
        browser.element('#submit-button').click()

    # @allure.step("Открывается страница с профилем")
    # def personal_account_entrance(self):
    #     browser.open('https://www.litres.ru/me/profile/')
    # # browser.element('[data-testid="user-button"]').click()
    #
    #
    # @allure.step("Проверяется успешность авторизации с валидными данными")
    # def should_have_authorized(self, value1, value2):
    #     browser.element('[data-testid="profile__userNameMain"]').should(
    #         have.text(value1)
    #     )
    #     browser.element('[data-testid="profile__logout--button"]').should(
    #         have.text(value2)
    #     )
    #
    # @allure.step("Проверяется неуспешная авторизация с невалидными данными")
    # def should_not_have_authorized(self, value1, value2, value3):
    #     browser.element('[data-testid="authorization-popup"]').should(be.visible)
    #     browser.element('[data-testid="auth__title"]').should(have.text(value1))
    #     browser.element('[data-testid="textbox--input__error"]').should(
    #         have.text(value2)
    #     )
    #     browser.element('[data-testid="auth__button--enter"]').should(have.text(value3))
    #
    # @allure.step("Проверяется неуспешная авторизация/пустое поле 'почта или логин'")
    # def login_cannot_be_empty(self, value1, value2):
    #     browser.element('[data-testid="authorization-popup"]').should(be.visible)
    #     browser.element('[data-testid="textbox--input__error"]').should(
    #         have.text(value1)
    #     )
    #     browser.element('[data-testid="auth__button--continue"]').should(
    #         have.text(value2)
    #     )