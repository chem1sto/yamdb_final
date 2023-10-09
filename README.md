# Проект YaMDb | Сбор отзывов пользователей на произведения.
### Индикатор состояния рабочих процессов
![API YaMDb Project CI/CD](https://github.com/chem1sto/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

### Краткое описание
YaMDb собирает отзывы пользователей на произведения (Titles).
Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка». Сами произведения в YaMDb не хранятся: нельзя посмотреть фильм или послушать музыку. Произведению может быть присвоен жанр (Genre) из списка предустановленных (например «Сказка», «Рок» или «Артхаус»). Новые произведения может добавлять только администратор, он же может расширять список категорий и жанров. 
Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят оценку в диапазоне от одного до десяти (целое число); из оценок формируется усреднённая оценка — рейтинг. На одно произведение пользователь может оставить только один отзыв.

Для приложения настроен Continuous Integration (CI) и Continuous Deployment (CD).

### Авторы
- Евгения Воропай | [jeniavoropay](https://github.com/jeniavoropay)
- Владимир Васильев | [chem1sto](https://github.com/chem1sto)
- Павел Вервейн | [hive937](https://github.com/hive937)

### Техно-стек
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
   ```bash
   git clone git@github.com:chem1sto/yamdb_final.git
   ```
2. Перейдите в него в командной строке:
   ```bash
   cd yamdb_final/
   ```
3. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   ```
   ```bash
   . venv/bin/activate
   ```
4. Обновите систему управления пакетами pip:
   ```bash
   python3 -m pip install --upgrade pip
   ```
5. Перейдите в папку api_yamdb и установите зависимости из файла requirements.txt
   ```bash
   cd api_yamdb
   ```
   ```bash
   pip install -r requirements.txt
   ```
6. Перейдите в директорию infra:
   ```bash
   cd cd ../infra/
   ```
7. Создайте файл .env с переменными окружения:
   ```bash
   touch .env
   ```
   ```bash
   nano .env
   ```
   ```text
   SECRET_KEY='<secret_key>'             # стандартный ключ, который создается при старте проекта
   PROD_FLAG=True                        # опция отладчика True/False
   ALLOWED_HOSTS=['*']                   # список хостов/доменов, для которых доступен текущий проект
   ENGINE=django.db.backends.postgresql  # используемый движок Postgres для работы базы данных
   DB_NAME=postgres                      # имя БД - postgres (по умолчанию)
   POSTGRES_USER=postgres                # логин для подключения к БД - postgres (по умолчанию)
   POSTGRES_PASSWORD=password            # пароль для подключения к БД (установите свой)
   DB_HOST=db                            # название сервиса (контейнера)
   DB_PORT=5432                          # порт для подключения к БД
   ```
8. Перейдите на уровень выше и запустите pytest:
   ```bash
   cd ..
   ```
   ```bash
   pytest
   ```
9. При push в ветку main автоматически отрабатывают сценарии:
    - Test Project - проверка кода на соответствие стандарту PEP8 и запуск pytest. Дальнейшие шаги выполняются, только если push был выполнен в ветку main;
    - Push Docker image to Docker Hub - сборка и доставка докер-образов на DockerHub
    - Deploy on Server - автоматический деплой проекта на боевой сервер. Выполняется копирование файлов из DockerHub на сервер;
    - Send message to Telegram - отправка уведомления в Telegram.

10. После успешного деплоя доступно создание суперпользователя:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```
### Ссылка на развернутый на виртуальном сервере проект
Доступен по ссылке [Сайт](http://185.17.3.67![img.png](img.png)/admin/login/?next=/admin/)

### Документация
[Redoc](http://51.250.2.221/redoc/)
