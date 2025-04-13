import os
import allure
from allure_commons.types import Severity
from selene import browser

from model.page_auth import AuthMOEX

moex_email = os.getenv("MOEX_EMAIL")
moex_password = os.getenv("MOEX_PASSWORD")


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Somebody")
@allure.feature("Авторизация пользователя")
@allure.story("Авторизация зарегистрированного пользователя через главную страницу")
@allure.link("https://github.com", name="Tests")
@allure.title("Авторизация с валидными данными")
def test_auth_valid_data(browser_settings):
    with allure.step('Открыть главную страницу'):
        auth_moex = AuthMOEX()
        auth_moex.open()
        # registration_page.remove_banners()
    with allure.step('Перейти на страницу авторизации'):
        auth_moex.press_tab_enter()
    with allure.step('Ввести валидные данные'):
        auth_moex.fill_email()
        auth_moex.fill_password()
    with allure.step('Авторизоваться'):
        auth_moex.press_tab_login()
    assert True