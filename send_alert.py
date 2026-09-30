

import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_IDS = [cid.strip() for cid in os.getenv("TELEGRAM_CHAT_ID", "").split(",") if cid.strip()]
# CHAT_IDS = os.getenv("TELEGRAM_CHAT_IDS", "").split(",") # Убрал  и подставил выше

run_number = os.getenv("GITHUB_RUN_NUMBER", "1")
report_url = "https://potter-yashka22.github.io/PythonProject_Griffonstyle_QA523/"

test_status = os.getenv("GH_STAGE_STATUS", "failed")

#  if-elif-else!
if test_status in ("success", "passed"):
    emoji_header = "🚀 **Дримтим, пайплайн на GitHub завершён!**"
    status_text = "🟢 **Статус тестов:** УСПЕШНО / PASSED"

elif test_status in ("failure", "failed"):
    emoji_header = "🚨🚨🚨 **ALARM!!! АТТЕНШН!!! ПОЛУНДРА!!!** 🚨🚨🚨"
    status_text = "🔴 **СТАТУС:** КРАШ! БАГ НА ПРОДЕ! КТО-ТО СЛОМАЛ СОРТИРОВКУ! 🌋"

else:
    emoji_header = "🟡 Дримтим, что-то пошло не так в облаке..."
    status_text = "⚪ **Статус:** Неизвестен"

# Сборка сообщения
message = f"""
{emoji_header}

🔢 **Сборка №:** #{run_number}
{status_text}
📊 **Смотреть Allure-отчёт:** [Кликни сюда]({report_url})
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

print(f"CHAT_IDS: {CHAT_IDS}")
for chat_id in CHAT_IDS:
    response = requests.post(url, json={
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    })

    if response.status_code == 200:
        print(f"✅Уведомление в чат {chat_id} успешно отправлено!")
    else:
        print(f"❌Ошибка отправки в {chat_id}: {response.text}")





















