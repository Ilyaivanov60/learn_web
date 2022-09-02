from unicodedata import name
from flask import Flask
from weather import weather_by_city


app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Moscow')
    if weather:
        return f'Погода {weather["temp_c"]}, ощущается как {weather["feelslike_c"]}'
    else:
        return 'Сервис погоды временно не доступпен'
if __name__ == '__main__':
    app.run(debug=True)