

import pytest
from src.sel import *
import allure
import time


@pytest.mark.unit
@allure.story("Проверка корректного отображения Email в ЛК пользователя")
def test_check_user_mail(login_akakiy):
    driver=login_akakiy
    with allure.step("Переход в раздел 'Общая информация'"):
        toClick(driver,By.LINK_TEXT,"Общая информация")
        time.sleep(1)
    with allure.step("Проверка что мы находимся на нужной вкладке"):
        actual_url=driver.current_url
        print(f"Текущий URL: '{actual_url}'")
        assert "?tab=commoninf" in actual_url, f"Ошибка! Неверный URL ЛК"
        subtitle_element=toFind(driver,By.CSS_SELECTOR,"div.myaccount-subtitle")
        actual_subtitle_text=subtitle_element.text
        print(f"Фактический подзаголовок: '{actual_subtitle_text}'")
        assert actual_subtitle_text=="Общая информация", f"Ошибка! текст подзаголовка не совпадает!"
    with allure.step("Проверка отображения правильного Email"):
        email_elem=toFind(driver,By.CSS_SELECTOR,'span[data-ng-init*="email"]')
        actual_email=email_elem.text
        print(f"Фактический Email в профиле: '{actual_email}'")
        assert email_elem.is_displayed()==True, "Ошибка! Поле Email не отображается!"
        assert "aleksacomp@mail.ru" in actual_email, f"Ошибка! На сайте отображается не верная почта!"
        assert getScreen(driver,107), "Ошибка! Не удалось сделать скриншот профиля!"


































