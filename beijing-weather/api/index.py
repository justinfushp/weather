from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/weather')
def weather():
    weather_data = get_weather()
    if weather_data:
        return jsonify({"success": True, "data": weather_data})
    return jsonify({"success": False, "message": "获取天气数据失败"})

if __name__ == '__main__':
    app.run(debug=True)