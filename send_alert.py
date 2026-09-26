

import os
import requests

TOKEN = "8865069128:AAHuiH8-R_qBCRr1vfJL6TlrgrO6lr05cUs"
CHAT_ID = "8328444589"

# Гитхаб во время сборки сам автоматически знает номер текущего прогона (RUN_NUMBER)
run_number = os.getenv("GITHUB_RUN_NUMBER", "1")
# Формируем прямую ссылку на Allure-отчет на твоем GitHub Pages
report_url = "https://github.com/Potter-Yashka22/PythonProject_Griffonstyle_QA523.git"

message = f"""
🚀 **Бро, пайплайн на GitHub завершён!**

🔢 **Сборка №:** #{run_number}
🟢 **Статус тестов:** УСПЕШНО / PASSED
📊 **Смотреть Allure-отчёт:** [Кликни сюда]({report_url})
"""
# Стучимся в официальные бэкенд-ворота Телеграма (API)
url = f"https://telegram.org{TOKEN}/sendMessage"

# Пуляем POST-запрос с JSON-телом, чтобы бот отправил сообщение в чат
response = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown",
    "disable_web_page_preview": True  # Чтобы ссылка не разворачивалась огромной картинкой
})

if response.status_code == 200:
    print("Уведомление в Телеграм успешно отправлено!")
else:
    print(f"Ошибка отправки: {response.text}")




















