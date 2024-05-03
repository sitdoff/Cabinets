#!/bin/bash
# Устанавливаем строгий режим
set -e

# Ожидание доступности базы данных
./wait-for-it.sh db:5432 -- echo "PostgreSQL is ready"

# Применение миграций, если это необходимо
python freelance/manage.py makemigrations && python freelance/manage.py migrate && python freelance/manage.py loaddata demo_data.json

# Запуск вашего Django приложения
exec "$@"
