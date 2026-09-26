
from src.helpers import validate_category_id
import pytest
import allure
from src.sel import *
import time


@pytest.mark.unit
@allure.story("Проверка валидности URL вкладки 'Крупный формат'")
def test_category_id_ui_integration(start):
    driver=start
    with allure.step("Проверка валидности URL вкладки 'Крупный формат' через Xpath"):
        large_format_locator="//span[text()='Крупный формат']"
        toClick(driver,By.XPATH,large_format_locator)
        time.sleep(1)
    with allure.step("Проверка типа данных и содержимого URL"):
        actual_url=driver.current_url
        print(f"Ткущий URL после клика: {actual_url}")
        assert isinstance(actual_url,str), "Ошибка! URL вернулся не в формате str"
        assert "krupnyi-format" in actual_url, f"Ошибка! 'krupnyi-format' отсутствует в строке URL"

































