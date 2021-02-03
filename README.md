## Инструкция по запуску сервиса

1.`git clone https://github.com/Foxonn/stilsoft_test_tast/tree/dev`
2.`docker-compose up --build`
3. Подключаемся к контейнеру django_app, и выполняет:
    1. `python manage.py migrate`
    2. `python manage.py loaddata stilsoft/fixtures/initial_data.json`
