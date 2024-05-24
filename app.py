from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key=AAJNBH6ATQ5LWNHMW9NGJFB6K&contentType=json'
        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = None
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
