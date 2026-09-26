
import pytest
import allure
from src.sel import *
import time

@pytest.mark.unit
@allure.story("Проверка работы выпадающего списка сортировки в каталоге")
def test_catalog_sorting_dropdown(start):
    driver=start
    with allure.step("Переход на вкладку 'Плитка'"):
        toClick(driver,By.LINK_TEXT,"Плитка")
        print("Переход на вкладку 'Плитка'")
        time.sleep(1)
        actual_url=driver.current_url
        assert "/podbor-plitki" in actual_url
        h1_title=toFind(driver,By.CSS_SELECTOR,".catalog-title h1")
        assert h1_title.is_displayed()==True
    with allure.step("Переход к сортировке и выбору 'Новинки' в селекторе"):
        sorting_selector=toFind(driver,By.ID,"Sorting")
        print("Прокрутка к элементу сортировки")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sorting_selector)
        toSelect(driver,By.ID,"Sorting","DescByAddingDate")
        time.sleep(2)
    with allure.step("Проверка что значение в селекторе успешно изменилось"):
        sorting_selector=toFind(driver,By.ID,"Sorting")
        actual_value=sorting_selector.get_attribute("value")
        print(f"Текущее значение в ID='Sorting': '{actual_value}'")
        assert actual_value=="DescByAddingDate", \
            f"Ошибка! Сортировка не переключилась на 'Новинки'. Получено: '{actual_value}'"
        assert getScreen(driver,106)





























