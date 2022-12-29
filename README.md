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
basedir = 'Путь к вашей db'
```
## Запуска программы 

Для автоматического парсинга запустите в отдельно окне терминал команду
```
celery -A tasks worker -B --loglevel=INFO
```
Запустите проект логально на своем компьютере ./run.sh