import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from src.sel import *




@pytest.fixture(scope='module')
def start():
    options=Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    driver=webdriver.Chrome(options=options)
    driver.set_page_load_timeout(5)
    try:
        driver.get('https://griffonstyle.ru/')
    except TimeoutException:
        print('Сайт не грузится')
    yield driver
    driver.quit()
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'start' in item.fixturenames:
                web_driver = item.funcargs['start']
                allure.attach(
                    web_driver.get_screenshot_as_png(),
                    name="Screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")

@pytest.fixture(scope='module')
def login_akakiy(start):
    driver=start
    with allure.step("Авторизация под валидными данными"):
        toClick(driver,By.CLASS_NAME,"site-head-login")
        time.sleep(1)
        toSend(driver,By.ID,"email","aleksacomp@mail.ru")
        toSend(driver,By.ID,"password","testerQA523")
        try:
            toClick(driver, By.XPATH, "//input[@value='Вход']")
        except Exception:
            print("Кнопка Вход исчезла во время клика, редирект пошел.")
        time.sleep(3)
    return driver















