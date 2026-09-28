

import os
import requests

TOKEN = "8865069128:AAHuiH8-R_qBCRr1vfJL6TlrgrO6lr05cUs"
CHAT_ID = "-1003843720000"


run_number = os.getenv("GITHUB_RUN_NUMBER", "1")
report_url = "https://github.com/Potter-Yashka22/PythonProject_Griffonstyle_QA523.git"

test_status = os.getenv("GH_STAGE_STATUS", "failed")

#  if-elif-else!
if test_status == "passed":
    emoji_header = "🚀 **Дримтим, пайплайн на GitHub завершён!**"
    status_text = "🟢 **Статус тестов:** УСПЕШНО / PASSED"
    sound_alert = True

elif test_status == "failed":
    emoji_header = "🚨🚨🚨 **ALARM!!! АТТЕНШН!!! ПОЛУНДРА!!!** 🚨🚨🚨"
    status_text = "🔴 **СТАТУС:** КРАШ! БАГ НА ПРОДЕ! КТО-ТО СЛОМАЛ СОРТИРОВКУ! 🌋"
    sound_alert = False

else:
    emoji_header = "🟡 Дримтим, что-то пошло не так в облаке..."
    status_text = "⚪ **Статус:** Неизвестен"
    sound_alert = True

# Сборка сообщения
message = f"""
{emoji_header}

🔢 **Сборка №:** #{run_number}
{status_text}
📊 **Смотреть Allure-отчёт:** [Кликни сюда]({report_url})
"""

url = f"https://telegram.org{TOKEN}/sendMessage"


response = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown",
    "disable_web_page_preview": True,
    "disable_notification": sound_alert
})

if response.status_code == 200:
    print("Уведомление в Телеграм успешно отправлено!")
else:
    print(f"Ошибка отправки: {response.text}")





















