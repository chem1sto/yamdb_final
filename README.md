# Учебный проект

### Индикатор состояния рабочих процессов
![Django-app workflow](https://github.com/chem1sto/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

### Краткое описание
Проект YaMDb собирает отзывы пользователей на произведения (Titles).
Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка». Сами произведения в YaMDb не хранятся: нельзя посмотреть фильм или послушать музыку. Произведению может быть присвоен жанр (Genre) из списка предустановленных (например «Сказка», «Рок» или «Артхаус»). Новые произведения может добавлять только администратор, он же может расширять список категорий и жанров. 
Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят оценку в диапазоне от одного до десяти (целое число); из оценок формируется усреднённая оценка — рейтинг. На одно произведение пользователь может оставить только один отзыв.

### Технологии
- Python 3.10
- Django 2.2.16
- Django Rest Framework 3.12.4
- Gunicorn 20.0.4
- Nginx
- Postgres
- Docker 20.10.23
- Docker Compose 2.15.1

### Запуск проекта
1. Клонируйте репозиторий:
```
git@github.com:chem1sto/infra_sp2.git
```
2. Перейдите в него в командной строке:
```
cd infra_sp2/
```
3. Cоздайте и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source env/bin/activate
```
4. Установите зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
5. Перейдите в папку infra_sp2/infra/
```
cd infra/
```
6. Выполните команду для развертывания приложения и его запуска:
```
docker compose up -d
```
7. Выполните миграции:
```
docker compose exec web python manage.py makemigrations reviews
```
```
docker compose exec web python manage.py migrate
```
8. Создайте суперпользователя:
```
docker compose exec web python manage.py createsuperuser
```
9. Соберите все статические файлы в папку static:
```
docker compose exec web python manage.py collectstatic --no-input 
```
10. Приложение активно и готово к использованию. Можно перейти по адресу http://localhost/admin/ и авторизоваться, введя свои данные от созданного суперпользователя.

### Документация
Доступна после запуска сервера: [Redoc](http://localhost/redoc/).

### Авторы
- Евгения Воропай | [jeniavoropay](https://github.com/jeniavoropay)
- Владимир Васильев | [chem1sto](https://github.com/chem1sto)
- Павел Вервейн | [hive937](https://github.com/hive937)
