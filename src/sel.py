import allure
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.step("Поиск элемента по локатору: {item}")
def toFind(driver,by,item):
    print(f'ищу элемент {item}')
    # f1=driver.find_element()
    e1=WebDriverWait(driver,5).until(
        EC.presence_of_element_located((by,item))
    )
    print(f'нашёл элемент {item}')
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", e1)
    except:
        print('Скролл не сработал')
    return e1

@allure.step("Клик по элементу: {item}")
def toClick(driver,by,item):
    toFind(driver,by,item)
    print(f'Проверка на клик {item}')
    e1 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((by, item))
    )
    e1.click()
    print(f'Кликнул на элемент {item}')
    return True

@allure.step("Ввод текста '{text}' в элемент: {item}")
def toSend(driver,by,item,text):
    f1=toFind(driver,by,item)
    f1.send_keys(text)
    f1.send_keys(Keys.ENTER)
    print(f'Вписал текст в {item}')
    try:
        p1=f1.get_attribute('value')
        print(f'текст виден {p1}')
    except:
        print('текст не виден')
    return True
@allure.step("Создание скриншота для отчёта")
def getScreen(driver,num):
    time.sleep(3)
    driver.get_screenshot_as_file(f'{num}.png')
    print(f'Скриншот {num} сохранён')
    return True

@allure.step("Выбор значения '{value}' в выпадающем списке: {item}")
def toSelect(driver, by, item, value):
    r1 = toFind(driver, by, item)
    print(f'Проверка на select {item}')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(r1)
    )
    select_element = Select(r1)
    select_element.select_by_value(value)
    print(f'Успешно выбрано значение {value} в элементе {item}')
    return r1











