# Учебный проект
### Индикатор состояния рабочих процессов
![Django-app workflow](https://github.com/chem1sto/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

### Краткое описание
Проект YaMDb собирает отзывы пользователей на произведения (Titles).
Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка». Сами произведения в YaMDb не хранятся: нельзя посмотреть фильм или послушать музыку. Произведению может быть присвоен жанр (Genre) из списка предустановленных (например «Сказка», «Рок» или «Артхаус»). Новые произведения может добавлять только администратор, он же может расширять список категорий и жанров. 
Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят оценку в диапазоне от одного до десяти (целое число); из оценок формируется усреднённая оценка — рейтинг. На одно произведение пользователь может оставить только один отзыв.

Для приложения настроен Continuous Integration (CI) и Continuous Deployment (CD).

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
### Запуск проекта
1. Клонируйте репозиторий:
```
git@github.com:chem1sto/yamdb_final.git
```
2. Перейдите в него в командной строке:
```
cd yamdb_final/
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
5. Создайте директорию .github/workflows:
```
mkdir .github/workflows
```
6. Скопируйте в созданную директорию файл yamdb_workflow.yml:
```
cp yamdb_workflow.yml .github/workflows/yamdb_workflow.yml
```
7. Перейдите в директорию infra:
```
cd infra/
```
8. Создайте файл .env с переменными окружения:
```
touch .env
```
```
nano .env
```
```
SECRET_KEY='<secret_key>'             # стандартный ключ, который создается при старте проекта
PROD_FLAG=True                        # опция отладчика True/False
ALLOWED_HOSTS                         # список хостов/доменов, для которых доступен текущий проект
ENGINE=django.db.backends.postgresql  # используемый движок Postgres для работы базы данных
DB_NAME                               # имя БД - postgres (по умолчанию)
POSTGRES_USER                         # логин для подключения к БД - postgres (по умолчанию)
POSTGRES_PASSWORD                     # пароль для подключения к БД (установите свой)
DB_HOST=db                            # название сервиса (контейнера)
DB_PORT=5432                          # порт для подключения к БД
```
9. Запустите pytest:
```
SECRET_KEY='<secret_key>' pytest
```
10. При push в ветку main автоматически отрабатывают сценарии:
- tests - проверка кода на соответствие стандарту PEP8 и запуск pytest. Дальнейшие шаги выполняются, только если push был выполнен в ветку main;
- build_and_push_to_docker_hub - сборка и доставка докер-образов на DockerHub
- deploy - автоматический деплой проекта на боевой сервер. Выполняется копирование файлов из DockerHub на сервер;
- send_message - отправка уведомления в Telegram.

### Ссылка на развернутый в облачном сервисе проект
[Yandex Cloud](http://51.250.2.221/admin/login/?next=/admin/).

### Документация
[Redoc](http://51.250.2.221/redoc/).

### Авторы
- Евгения Воропай | [jeniavoropay](https://github.com/jeniavoropay)
- Владимир Васильев | [chem1sto](https://github.com/chem1sto)
- Павел Вервейн | [hive937](https://github.com/hive937)
