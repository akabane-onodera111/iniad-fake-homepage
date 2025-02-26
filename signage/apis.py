from urllib import request, parse
import json
from datetime import datetime
from pytz import timezone

#GEOCODING_URL = ***
#GOOGLE_APIKEY = ***

#WEATHER_URL = ***
#WEATHER_APPID = ***

def address_to_latlng(address):
  params = {
    'key' : GOOGLE_APIKEY,
    'address' : address,
    'language' : 'ja'
  }
    
  url = GEOCODING_URL + '?' + parse.urlencode(params)
  res = request.urlopen(url)
  result = json.loads(res.read().decode('utf-8'))
  res.close()
  

  loc = result['results'][0]['geometry']['location']

  return (loc['lat'], loc['lng'])

def get_weather(latitude, longitude):
  params = {
    'appid': WEATHER_APPID,
    'lat': latitude,
    'lon' : longitude,
    'units' : 'metric'
  }

  url = WEATHER_URL + '?' + parse.urlencode(params) 
  req = request.Request(url)
  res = request.urlopen(req)
  data = json.loads(res.read().decode('utf-8'))
  res.close()

  result = []
  for item in data['list']:
    date = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S').astimezone(timezone('Asia/Tokyo'))
    weather = {
      'date' : date.strftime('%Y-%m-%d %H:%M'),
      'weather' : item['weather'][0]['main'],
      'temperature' : item['main']['temp'],
      'pressure' : item['main']['pressure'],
      'humidity' : item['main']['humidity'],
    }
    result.append(weather)

  return result
