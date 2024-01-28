from flask import Flask, render_template, request
from urllib import parse
import apis

app = Flask(__name__)

@app.route('weather_tokyo.html', methods=['GET', 'POST'])
def weather():
  city = '東京都北区赤羽台'
  if request.method == 'POST':
    city = request.form['keyword']
  lat,lng = apis.address_to_latlng(city)
  forecast = apis.get_weather(lat, lng)

  return render_template('weather_tokyo.html', city=city, lat=lat, lon=lng, forecast=forecast)

if __name__ == '__main__':
  app.run(host='0.0.0.0')