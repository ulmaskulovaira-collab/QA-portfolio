# Тестирование · работы Ирины Ульмаскуловой

[← На главную](../README.md) · [Мини-проекты Python](../05-python-mini-projects/README.md)

Здесь собраны **QA-работы**. В каждой папке есть README: что проверялось, какие файлы открыть и что именно они показывают. PDF и таблицы относятся к учебным заданиям; код автотестов открыт в соответствующих папках.

## Ручное тестирование

| Папка | Задача | Что открыть |
| --- | --- | --- |
| [01 · Яндекс Маршруты](./01-yandex-routes/README.md) | функциональные проверки и расчёты | [таблица с кейсами и багами](./01-yandex-routes/test-design-cases-bugs.xlsx), [PDF](./01-yandex-routes/report.pdf) |
| [02 · Каршеринг](./02-carsharing-layout/README.md) | интерфейс и бронирование | [чек-лист и баги](./02-carsharing-layout/layout-checklist-bugs.xlsx), [PDF](./02-carsharing-layout/report.pdf) |
| [03 · Место](./03-mesto-regression/README.md) | регрессионная проверка | [чек-лист](./03-mesto-regression/regression-checklist.xlsx), [PDF](./03-mesto-regression/report.pdf) |
| [05 · Web, API и SQL](./05-manual-qa-practice/README.md) | сценарии и примеры проверок | [Web](./05-manual-qa-practice/saucedemo-web.md), [API](./05-manual-qa-practice/booking-api.md), [SQL](./05-manual-qa-practice/validation_queries.sql) |

[Примеры баг-репортов из первых трёх работ](./BUGS-SUMMARY.md).

## Автотестирование и данные

| Папка | Задача | Что открыть |
| --- | --- | --- |
| [04 · SauceDemo](./04-playwright-saucedemo/README.md) | UI-сценарии на Python + Playwright + pytest | [26 тестовых функций](./04-playwright-saucedemo/tests), [Page Object](./04-playwright-saucedemo/pages) |
| [06 · Заказы](./06-order-data-tests/README.md) | Python + SQLite + SQL | [автотесты](./06-order-data-tests/tests/test_orders.py), [диагностические запросы](./06-order-data-tests/validation_queries.sql) |

**С чего начать:** если интересует ручное тестирование — откройте проект 01 или 05; если код — проекты 04 и 06. Команды запуска указаны в README каждого проекта. Мини-программы и игры на Python находятся [на главной странице](../README.md#python-отдельно-от-qa).

[Telegram](https://t.me/Seein_tan) · [Email](mailto:ulmaskulovaira@gmail.com)
