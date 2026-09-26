
import pytest
from src.sel import *
import allure
import time


@pytest.mark.unit
@allure.story("Проверка кликабельности email в футере сайта")
def test_email_link_protocol(start):
    driver=start
    with allure.step("Поиск элемента с почтой в футере сайта"):
        f1=toFind(driver,By.CSS_SELECTOR,'a[href^="mailto:"]')
        start.execute_script("arguments[0].scrollIntoView({block: 'center'});",f1)
        visible_txt=f1.text
        print(f"Текст почты на сайте: '{visible_txt}'")
    with allure.step("Валидация протокола mailto: для вызова почтового клиента"):
        actual_href=f1.get_attribute("href")
        print(f"Значение атрибута href: '{actual_href}'")
        assert actual_href is not None, "Ошибка! У элемента почты отсутствует атрибут href!"
        assert actual_href.startswith("mailto"), f"Ошибка! Ссылка не использует протокол mailto"
        expected_email="mailto:info@griffonstyle.ru"
        assert actual_href==expected_email, f"Ошибка! Адрес почты в href не совпадает!"



























