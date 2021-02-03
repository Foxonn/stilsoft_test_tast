## Инструкция по запуску сервиса на docker

`git clone -b dev https://github.com/Foxonn/stilsoft_test_tast/`

`cd stilsoft_test_tast`

`docker-compose up --build`

Подключаемся к контейнеру django_app, и выполняет:
1. `python manage.py migrate`
2. `python manage.py loaddata stilsoft/fixtures/initial_data.json`

Перезапустить все контейнеры

http://localhost:8080/api/v1/blog/

Пользователи:
login: admin pass: 185335
login: manager pass: drmjSV&CC^Br

Документация
- http://localhost:8080/swagger/
- http://localhost:8080/redoc/
