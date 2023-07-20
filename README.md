# online_store

## Описание
Online-store - это многостраничное веб-приложение. Позволяет пользователям создавать аккаунты, добавлять товары в корзину и производить тестовую онлайн-оплату.
Используется сервер Gmail для отправки электронной почты из приложенияпо протоколу SMTP.
Интегрирована возможность тестовой онлайн оплаты корзины и разместить заказ.

## Технологии
Python 3.7
Django 2.2.19
Celery
Rabbitmq
SMTP (Gmail)
HTML 5
JavaScript
css

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
### Авторы
Леонтьев Павел
