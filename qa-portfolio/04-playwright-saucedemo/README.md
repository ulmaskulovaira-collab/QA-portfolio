# Автоматизация UI — SauceDemo (Playwright + Python)

**Автор портфолио:** Ирина Ульмаскулова  
**Тип:** End-to-end UI-автотесты  
**Паттерн:** Page Object Model (POM)  
**Стек:** Playwright · Python · pytest  
**Приложение:** [SauceDemo](https://www.saucedemo.com)

## О проекте

Фреймворк UI-автотестов для учебного интернет-магазина SauceDemo.  
26 тестов покрывают основные пользовательские сценарии: авторизация, каталог, корзина, оформление заказа.

| Модуль | Тестов | Покрытие |
|--------|--------|----------|
| Login | 7 | Успешный вход, неверный пароль, пустые поля, ввод в поля |
| Products | 7 | Список товаров, имена, цены, кнопки, изображения, детали |
| Cart | 7 | Бейдж, добавление/удаление, переход в корзину |
| Checkout | 5 | Форма, валидация, полный happy-path |
| **Итого** | **26** | Полный e-commerce workflow |

## Структура

```
04-playwright-saucedemo/
├── pages/
│   ├── base_page.py        # Базовый класс (навигация, wait)
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
├── pytest.ini
├── requirements.txt
├── report.pdf              # Отчёт о проекте
└── README.md
```

## Стек и подходы

- **Playwright** (sync API) — автоматизация браузера
- **pytest** + pytest-playwright
- **Page Object Model** — локаторы и действия в page-классах, тесты без дублирования селекторов
- `data-test` атрибуты для стабильных локаторов
- Проверки через `expect()` (auto-wait)

## Быстрый старт

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium

pytest tests/ -v
# с видимым браузером:
pytest tests/ -v --headed
```

## Конфигурация (`pytest.ini`)

```ini
[pytest]
addopts = -v --headed --slowmo=500
python_files = test_*.py
base_url = https://www.saucedemo.com
```

## Пример Page Object

```python
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
```

## Что демонстрирует проект

- Умение строить поддерживаемый UI-фреймворк
- Разделение page objects и тестов
- Покрытие happy-path и негативных сценариев (ошибки логина, пустые поля checkout)
- Готовность к расширению (другие браузеры, CI, отчёты)

## Планы развития

- [ ] Firefox / WebKit
- [ ] GitHub Actions CI
- [ ] Allure / HTML-отчёт
- [ ] Скриншоты и video при падении
- [ ] Параллельный прогон
