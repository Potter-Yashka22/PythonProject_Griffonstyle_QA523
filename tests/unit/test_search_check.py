
import pytest
from src.sel import *
from src.helpers import clean_search_query
import allure
import time

from tests.conftest import start


@pytest.mark.unit
@allure.story("Проверка взаимодействия поисковых запросов с БД ")
def test_search_query_cleaning_unit(start):
    driver=start
    with allure.step("Клик по иконке лупы (Поиск)"):
        toClick(driver,By.ID,"change-icon")
        print("Кликнул по иконке Поиск")
        time.sleep(1)
    with allure.step("Ввод поискового запроса с лишними пробелами"):
        search_input_locator = "#search-block input"
        toSend(driver,By.CSS_SELECTOR,search_input_locator, "   плитка   ")
        print("Отправил поисковый запрос с пробелами")
        time.sleep(1)
    with allure.step("Проверка очистки строки от пробелов"):
        search_field=toFind(driver,By.CSS_SELECTOR,"#search-block input")
        actual_value=search_field.get_attribute("value")
        print(f"Значение в поле поиска: '{actual_value}'")
        assert actual_value.strip()=="плитка", f"Ошибка! Пробелы не очистились!"
        assert getScreen(driver,109)



































