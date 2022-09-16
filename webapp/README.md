# Новостной сайт python 

Программа парсит новости с [сайта python.org](https://www.python.org/blogs/) и выводит на наш сайт.

## Установака

скачайте проект с gitgub и установите зависимости

```
git clone ttps://github.com/Ilyaivanov60/learn_web.git
```

Создайте вертуальное окружение и установите зависимоти:
```
pip install -r requirements.txt
```

Создайте файл confg.py и создайте в нем базовые переменные
```
WEATHER_DEFAULT_CITY = "Выберите город"
WEATHER_API_KEY = api key с сайта https://www.weatherapi.com/
WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + к вашей db

SECRET_KEY = 'ваш secter key'
```
## Запуска программы 

добавить информацию по запуску програмы