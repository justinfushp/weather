from app import app
import pytz

@app.route('/')
def home():
    return "Server is running!"