# api_final
api final
# Yatube API

REST API для социальной сети Yatube. Позволяет публиковать посты, оставлять комментарии, подписываться на авторов и объединять посты в тематические группы.

## Возможности

- Просмотр постов и групп (доступно всем).
- Создание, редактирование и удаление постов и комментариев (только для авторизованных пользователей, изменение только своего контента).
- Подписка на авторов и просмотр своих подписок.
- Поиск по подпискам.
- JWT-аутентификация.

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/yourusername/yatube_api.git
   cd yatube_api
2. Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
3. Установите зависимости:
pip install -r requirements.txt
4. Выполните миграции:
python manage.py migrate
5. Запустите сервер:
python manage.py runserver