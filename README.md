# CakeBake

Сайт магазина тортов с возможностью самостоятельной сборки торта покупателем. Предусмотрена оплата заказов через [ЮKassa](https://yookassa.ru/).

## Запуск

Для запуска в системе должен быть установлен Python 3.

- Скачайте код
- Создайте и активируйте виртуальное окружение командой 
```bash
python3 -m venv env && source env/bin/activate
```
- Установите зависимости командой
```bash
pip install -r requirements.txt
```
- Создайте в корне проекта файл `.env` с переменными окружения:

  <pre>
  SECRET_KEY=*секретный ключ проекта, например `erofheronoirenfoernfx49389f43xf3984xf9384`*
  DEBUG=*дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`*
  SHOP_ID=*идентификатор магазина из <a href="https://yookassa.ru/my">личного кабинета</a> ЮKassa*
  YOOKASSA_API_KEY=*ключ для аутентификации запросов к ЮKassa. Нужно получить в <a href="https://yookassa.ru/my/merchant/integration/api-keys">личном кабинете</a>*
  EMAIL_HOST=*адрес smtp-сервера например `smtp.gmail.com`*
  EMAIL_PORT=*порт smtp-сервера*
  EMAIL_USE_TLS=True
  EMAIL_HOST_USER=*email, с которого будет отправляться письмо пользователю после регистрации*
  EMAIL_HOST_PASSWORD=*пароль приложения, генерируется в настройках почтового аккаунта* 
  </pre>
- Создайте базу данных и примените миграции командами
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
- Создайте учётную запись администратора командой
```bash
python3 manage.py createsuperuser
```
- Запустите сервер командой
```bash
python3 manage.py runserver
```

После этого главная страница будет доступна по адресу [127.0.0.1:8000](http://127.0.0.1:8000), админка — [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Цели проекта

Основа сайта предоставлена командой [Devman](https://dvmn.org).  
Backend прописан командой разработчиков проекта.
