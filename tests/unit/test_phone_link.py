
import pytest
from src.sel import *
import allure
import time

@pytest.mark.unit
@allure.story("Проверка кликабельности номера телефона в шапке сайта")
def test_phone_link_click(start):
    driver=start
    with allure.step("Поиск элемента с номером телефона в шапке"):
        phone_el=toFind(driver,By.CSS_SELECTOR,"a.site-head-phone")
        visible_text=phone_el.text
        print(f"Текст телефона на сайте: '{visible_text}'")
        assert phone_el.get_attribute("href") is not None, f"Ошибка! У элемента телефона нет атрибута href! "
    with allure.step("Валидация протокола tel: для вызова приложения"):
        actual_href=phone_el.get_attribute("href")
        print(f"Значение атрибута href: '{actual_href}'")
        assert actual_href.startswith("tel"), f"Ошибка! Протокол tel не найден:{actual_href}"
        assert "495" in actual_href, f"Ошибка! Код города не найден в href!"
        assert "127-71-06" in actual_href, f"Ошибка! Хвост номера не найден в href!"



















