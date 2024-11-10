#!/bin/bash
case "$1" in
# Запуск контейнера
    up)
        echo "Запуск Docker Compose..."
        docker compose up -d
        ;;
# Остановка и удаление контейнеров
    down)
        echo "Остановка Docker Compose..."
        docker compose down
        ;;
    build)
        echo "Остановка Docker Compose..."
        docker compose build
        ;;
#------------------------------------------------#
# manage.py команды
# docker compose exec backend-django python -Xutf8 manage.py dumpdata books.Book > backend_books_review/books/fixtures/books_fixtures.json
# docker compose exec backend-django python -Xutf8 manage.py loaddata books/fixtures/books_fixtures.json
    makemigrations)
        echo "Создание миграций..."
        docker compose exec backend-django python manage.py makemigrations
        ;;
    migrate)
        echo "Мигрирование..."
        docker compose exec backend-django python manage.py migrate
        ;;
    createsuperuser)
        echo "Создание супер-пользователя..."
        docker compose exec backend-django python manage.py createsuperuser
        ;;
    startapp)
        if [ -z "$2" ]; then
            echo "Ошибка: Укажите имя приложения."
            exit 1
        fi
        APP_NAME="$2"
        echo "Создание приложения '$APP_NAME'..."
        cd backend_books_review
        django-admin startapp "$APP_NAME"
        ;;
#------------------------------------------------#
# остальные команды
    freeze)
        echo "Обновление зависимостей..."
        pip freeze > backend_books_review/requirements.txt
        ;;
    isort)
        echo "Запуск isort..."
        isort ./backend_books_review
        ;;
    *)
        echo "Данной команды не существует."
        exit 1
        ;;
esac
