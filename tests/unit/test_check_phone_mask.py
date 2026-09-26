

import pytest
from src.sel import *
import allure
import time

@pytest.mark.unit
@pytest.mark.xfail(reason="Критический баг: маска Angular искажает номер пользователя")
@allure.story("Проверка маски телефона в форме обратной связи")
def test_check_phone_mask(login_akakiy):
    driver=login_akakiy
    with allure.step("Переход на страницу формы обратной связи"):
        toClick(driver,By.LINK_TEXT,"Студия мозаики")
        print("Переход на нужную вкладку")
        time.sleep(16)
    with allure.step("Проверка заголовка h1"):
        actual_url=driver.current_url
        print(f"Текущий URL: '{actual_url}'")
        time.sleep(2)
        assert "/studiya-mozaiki" in actual_url
        h1_title=toFind(driver,By.CSS_SELECTOR,".catalog-title h1")
        actual_h1_text=h1_title.text
        print(f"Фактический заголовок на странице: '{actual_h1_text}'")
        assert h1_title.is_displayed()==True, f"Ошибка! Заголовок H1 е отображается!"
        expected_h1_text="Индивидуальное панно из мозаики по вашим эскизам"
        assert actual_h1_text==expected_h1_text, f"Ошибка! Текст заголовка не совпадает!"
    with allure.step("Скролл вниз страницы к форме обратной связи"):
        phone_field=toFind(driver,By.CSS_SELECTOR,"input.lp-form__field_phone")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",phone_field)
    with allure.step("Локализация бага и финальный скриншот"):
        actual_phone=phone_field.get_attribute("value")
        print(f"Фактическое значение в поле телефона: '{actual_phone}'")
        assert getScreen(driver,108)
        expected_clean="89209205285"
        assert expected_clean in actual_phone.replace(" ",""), \
            f"Критический баг! Макса Angular исказила номер пользователя! Получено: '{actual_phone}'"

























