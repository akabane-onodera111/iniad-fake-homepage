from flask import Flask, render_template, request
from urllib import parse
import apis
import jinja2 import Template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
  city = '東京都北区赤羽台'
  if request.method == 'POST':
    city = request.form['keyword']
  lat,lng = apis.address_to_latlng(city)
  forecast = apis.get_weather(lat, lng)

  return render_template('weather_tokyo.html', city=city, lat=lat, lng=lng, forecast=forecast)

@app.route('/weather_tokyo.html')
def test_print():
  weather = "cloud" #仮置き
  return render_template('weather_tokyo.html', weather=weather)

if __name__ == '__main__':
  app.run(host='0.0.0.0')