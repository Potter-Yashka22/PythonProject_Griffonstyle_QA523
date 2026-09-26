import pytest
from src.helpers import generate_random_email


def test_email_generation_format():
    email=generate_random_email("valera")
    print(f"Сгенерированный email: {email}")
    assert "@" in email, " В email отсутствует символ @"
    assert "valera_" in email, "Email не начинается с базового имени"
    assert email.endswith("@griffonstyle.ru"), "Неверный домен почты"






