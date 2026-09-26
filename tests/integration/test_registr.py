import time
from threading import activeCount
from src.helpers import generate_random_email
import pytest
import allure
from src.sel import *

@pytest.mark.integration
@allure.story('Регистрация нового пользователя')
@allure.step('Переход на страницу авторизации/регистрации')
def test_get_auth_0(start):
    log_icon_locator=".site-head-login"
    print("Кликаю на иконку Login")
    toClick(start,By.CSS_SELECTOR,log_icon_locator)
    time.sleep(3)
    with allure.step("Проверка, что в URL присутствует '/login'"):
        current_url = start.current_url
        print(f"Текущий URL сайта: {current_url}")
        assert "login" in current_url, f"Ожидали увидеть 'login' в URL, но получили: {current_url}"
    with allure.step("Проверка наличия заголовка 'Авторизация'"):
        header_locator = "h1.main-login-title"
        header_el=toFind(start,By.CSS_SELECTOR,header_locator)
        header_text=header_el.text.strip()
        print(f"Текст найденного заголовка: {header_text}")
        assert header_text=="Авторизация", f"Ожидали заголовок 'Авторизация', но нашли: '{header_text}'"
    with allure.step("Переход к регистрации по кнопке 'Регистрация'"):
        reg_btn_locator="a.btn-confirm"
        toClick(start,By.CSS_SELECTOR,reg_btn_locator)
        time.sleep(2)
    with allure.step("Проверка, что URL изменился на '/registration'"):
        current_url=start.current_url
        print(f"Текущий URL после клика на регистрацию: {current_url}")
        assert "registration" in current_url, f"Ожидали увидеть 'registration' в URL, но получили: {current_url}"
        page_source=start.page_source
        assert "Регистрация" in page_source, "Заголовок 'Регистрация' найден на странице!"
    with allure.step("Заполнение личных данных в анкете регистрации"):
        test_name = "Акакий"
        toSend(start,By.ID,"FirstName",test_name)
        time.sleep(1)
    with allure.step(f"Проверка, что в поле 'Имя' записалось значение: '{test_name}'"):
        actual_name_value = toFind(start, By.ID, "FirstName").get_attribute("value")
        print(f"Фактическое значение в поле Имя: {actual_name_value}")
        assert actual_name_value==test_name, f"Ожидалось '{test_name}', а вписано: '{actual_name_value}'"
    with allure.step("Заполняю поле 'Фамилия'"):
        test_surname="Эчпочмаков"
        toSend(start,By.ID,"LastName",test_surname)
        time.sleep(2)
    with allure.step(f"Проверка, что в поле 'Фамилия' записалось значение: '{test_surname}'"):
        actual_surname_value=toFind(start,By.ID,'LastName').get_attribute("value")
        print(f"Фактическое значение в поле Фамилия: {actual_surname_value}")
        assert actual_surname_value==test_surname, f"Ожидалось '{test_surname}', а вписано: '{actual_name_value}'"
    with allure.step("Заполняю поле 'E-Mail'"):
        test_email=generate_random_email("akakiy")
        toSend(start,By.ID,"Email",test_email)
        time.sleep(1)
    with allure.step("Проверка корректности заполнения поля 'Email'"):
        actual_email_value=toFind(start,By.ID,"Email").get_attribute("value")
        print(f"Фактическое значение в поле почта '{actual_email_value}'")
        assert actual_email_value==test_email, f"Ожидалось '{test_name}', а получили '{actual_name_value}'"
    with allure.step("Посимвольный ввод номера телефона"):
        test_phone="89209205285"
        phone_field=toFind(start,By.ID, "Phone")
        phone_field.clear()
        for digit in test_phone:
            phone_field.send_keys(digit)
            time.sleep(1)
    with allure.step(f"Проверка, что в поле 'Телефон' записался верный номер: '{test_phone}'"):
        actual_phone_numb=toFind(start,By.ID,"Phone").get_attribute("value")
        print(f"Фактическое значение в поле Телефон: {actual_phone_numb}")
        assert "920" in actual_phone_numb, f"Ожидали увидеть часть номера в маске, но получили: '{actual_phone_numb}'"
    with allure.step("Заполняю поля 'Password' и 'PasswordConfirm'"):
        test_pass="testerQA523"
        toSend(start,By.ID,"Password",test_pass)
        toSend(start,By.ID,"PasswordConfirm", test_pass)
        time.sleep(1)
    with allure.step("Проверка что поля паролей успешно заполнены"):
        actual_pass=toFind(start,By.ID,"Password").get_attribute("value")
        actual_confirm_pass=toFind(start,By.ID,"PasswordConfirm").get_attribute("value")
        print(f"Фактическое значение в поле Пароль: '{actual_pass}'")
        print(f"Фактическое значение в поле Подтверждение пароля: '{actual_confirm_pass}'")
        assert len(actual_pass)>0, "Ошибка! Первое поле осталось пустым!"
        assert len(actual_confirm_pass)>0, "Ошибка! Поле подтверждения пароля осталось пустым!"
        assert actual_pass==actual_confirm_pass, "Ошибка! Пароли в полях не совпадают!"
    with allure.step("Выбор сферы деятельности через стандартный select"):
        select_id="CustomerFields_0__Value"
        toSelect(start,By.ID,select_id,"Частный покупатель")
        time.sleep(1)
    with allure.step("Проверка выбранной роли 'Частный покупатель'"):
        actual_role=toFind(start,By.ID,"CustomerFields_0__Value").get_attribute("value")
        print(f"Фактическое значение в поле сфера деятельности: '{actual_role}'")
        assert actual_role=="Частный покупатель", f"Ошибка! Ожидали роль 'Частный покупатель', но система выдала '{actual_role}'"
    with allure.step("Пауза: Ручной ввод капчи пользователем"):
        print("\n⚠️ [Внимание] Тест приостановлен на 25 секунд для ввода капчи!")
        captcha_locator = "CaptchaCode"
        capcha_field=toFind(start,By.ID,captcha_locator)
        start.execute_script("arguments[0].scrollIntoView({block: 'center'});", capcha_field)
        time.sleep(1)
        capcha_field.click()
        time.sleep(25)
        print("Делаю скриншот")
        assert getScreen(start,101)
    with allure.step("Клик по чек-боксу согласия с ПД"):
        checkbox_btn="span.custom-input-checkbox"
        toClick(start,By.CSS_SELECTOR,checkbox_btn)
        time.sleep(1)
    with allure.step("Проверка, что чек-бокс активирован"):
        actual_checkbox_btn=toFind(start,By.ID,"Agree")
        is_checked=actual_checkbox_btn.is_selected()
        print(f"Статус чек-бокса в системе (is_selected): {is_checked}")
        assert is_checked==True, "Ошибка! Чек-бокс не активирован!"
    with allure.step("Переход по кнопке 'Зарегистрироваться'"):
        toClick(start,By.CSS_SELECTOR,"input.btn-submit.group-reg")
        time.sleep(4)
        assert getScreen(start,102)
    with allure.step("Проверяю переход на главую страницу после регистрации и появление ЛК"):
        current_url=start.current_url
        print(f"URL-адрес после регистрации: {current_url}")
        assert "registration" not in current_url, f"Ошибка! Переход на главную после регистрации не состоялось!"
























