#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Автоматически загружаем тестовые данные и создаем пользователей
python load_data.py

