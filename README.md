# python_kfu
> Основы разработки проекта с фреймворком Django

## Запуск проекта
- `python3 -m venv venv` - создание виртуального окружения
- `source venv/bin/activate` - войти в виртуальное окружение
- `pip install -r requirements.txt` - установка зависимостей
- `python manage.py migrate` - примененить миграции
- `python manage.py runserver` - запустить сервер для разработки

## Добавление бд
- ` psql -U postgres -d postgres`
- `CREATE DATABASE timetracker;`
- `ALTER USER postgres WITH PASSWORD 'postgres';`
