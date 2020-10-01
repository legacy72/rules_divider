# Приложение показывает пример раграничения прав пользователей 

### Запуск локально
* `virtualenv .env -p python3.8`
* `source .env/bin/activate`
* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py runserver`

### Создание суперпользователя
* `python manage.py createsuperuser`

### Для демонстрации разграничения прав
1. Создать группы для соответсвующего доступа в панели администратора:
    * books
    * films
    * musics
2. Раздать пользователям нужные группы

