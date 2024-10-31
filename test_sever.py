from flask import Flask, jsonify
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
def get_weather():
    try:
        url = "https://wttr.in/Beijing?format=j1"
        response = requests.get(url, verify=False)
        data = response.json()['current_condition'][0]
        
        return {
            'temperature': data['temp_C'],
            'humidity': data['humidity'],
            'description': data['weatherDesc'][0]['value'],
            'feels_like': data['FeelsLikeC'],
            'wind_speed': data['windspeedKmph'],
            'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        return None

@app.route('/', methods=['GET'])
def home():
    return "测试服务器运行正常！"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)