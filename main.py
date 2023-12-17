










import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys
API_KEY = "bb0033061aaab3054af8bbbd53335300"
city = "Dnipro,ua"

lat, lon = 46.482952, 30.712481
def kelvin_to_celsius(kelvin_temperature):
    return kelvin_temperature - 273.15
def get_weather_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        city_name = data["name"]
        temp_celsius = round(kelvin_to_celsius(data["main"]["temp"]), 2)
        weather_description = data["weather"][0]["description"]
        return {
            "city": city_name,
            "temp_celsius": temp_celsius,
            "weather_desc": weather_description
        }
    except Exception as e:
        print("Error", e)
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
weather_data = get_weather_data(url)
# print(f"1. Місто: {weather_data['city']}\n2. Температура: {weather_data['temp_celsius']} \n3. Опис погоди: {weather_data['weather_desc']}")

app = QApplication([])
window = QWidget()
window.resize(400, 300)

try:
    with open("./style.css", 'r') as styles:
        style_sheet = styles.read()
except:
    print("Error file was not found")

app.setStyleSheet(style_sheet)
city_label = QLabel(f"City: {weather_data['city']}")
temp_label = QLabel(f"Temperature: {weather_data['temp_celsius']}")
weather_label = QLabel(f"Weather: {weather_data['weather_desc']}")
layout = QVBoxLayout()

layout.addWidget(city_label)
layout.addWidget(temp_label)
layout.addWidget(weather_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
