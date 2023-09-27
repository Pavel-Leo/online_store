# online_store
Работу сервиса можно посмотреть по адресу https://coffeechai.pythonanywhere.com/

## Описание
Online-store - это многостраничное веб-приложение.
Позволяет пользователям создавать аккаунты, добавлять товары в корзину и производить тестовую онлайн-оплату.
Используется сервер Gmail для отправки электронной почты из приложенияпо протоколу SMTP.
Интегрирована возможность тестовой онлайн оплаты корзины и разместить заказ.

Ниже приведены тестовые данные, которые вы можете использовать для различных сценариев тестирования:

Успешные тестовые платежи:
```
Номер карты: 4242 4242 4242 4242
Срок действия: Любая будущая дата
CVC: Любое трехзначное число
Имя и фамилия: Любое имя и фамилия на латинице
```

Неуспешные тестовые платежи:
```
Номер карты: 4000 0000 0000 0002 (карта отклоняется)
Номер карты: 4000 0000 0000 0069 (платеж требует аутентификации)
Другие специальные случаи:

Номер карты: 4000 0027 6000 3184 (автоматически отклоняется как дубликат транзакции)
```

## Технологии
Python 3.7,
Django 3.2.16,
Celery,
Rabbitmq,
SMTP (Gmail),
HTML 5,
JavaScript,
css.

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Pavel-Leo/online_store.git
```

```
cd online_store
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv (для mac и linux)
python -m venv venv (для windows)
```

```
source venv/bin/activate (для mac и linux)
source venv/Scripts/activate (для windows)
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip (для mac и linux)
python -m pip install --upgrade pip (для windows)
```

```
перейти в дирректорию где хранится файл requirements.txt и оттуда выполнить команду:

pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate (для mac и linux)
python manage.py migrate (для windows)
```

Запустить проект:

```
перейти в дирректорию где хранится файл manage.py и оттуда выполнить команду:

python3 manage.py runserver (для mac и linux)
python manage.py runserver (для windows)
```

## Как запустить проект c помощью docker:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Pavel-Leo/online_store.git
```

```
cd online_store
```

:exclamation: Идеально было бы в корневой папке там же где располагаются репозитории backend, frontend и тд создать файл .env. Заполнение файла можно взять из .env.example или из кода ниже:

```
SECRET_KEY='kb23&&e3h52665ng&9af=y_-h_-2j5t97wlqxja6gg$$_0jpu'
DEBUG=False
ALLOWED_HOSTS='localhost,127.0.0.1,ваш IP адрес,ваш домен'
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
DB_NAME=postgres
DB_HOST=db
DB_PORT=5432
```

Из корневой папки где находится файл docker-compose.yml выполнить команды по очереди:

```
docker compose up
docker compose -f docker-compose.yml exec backend python manage.py makemigrations
docker compose -f docker-compose.yml exec backend python manage.py migrate
docker compose -f docker-compose.yml exec backend python manage.py collectstatic

если вы работате на windows в git bash то следующую команду следует выполнить из Windows PoweShell из того же репозитория где находится файл docker-compose.yml чтобы пути построились верно:
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/

Создайте суперпользователя:
docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```

Теперь вы можете перейти по адресу http://localhost:8000/  и пользоваться приложением.
### Авторы
Леонтьев Павел
