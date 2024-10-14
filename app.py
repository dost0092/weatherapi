from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # default city
        city = 'New York'

    # Your WeatherAPI key here
    api_key = "8cde9026006740bfa8e51742241410"

    # WeatherAPI request URL (replace with WeatherAPI's endpoint)
    api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    # Fetching the weather data
    try:
        source = urllib.request.urlopen(api_url).read()
        list_of_data = json.loads(source)

        data = {
            "city": city,
            "country": list_of_data['location']['country'],
            "coordinate": f"{list_of_data['location']['lat']}, {list_of_data['location']['lon']}",
            "temp_c": f"{list_of_data['current']['temp_c']} °C",
            "temp_f": f"{list_of_data['current']['temp_f']} °F",
            "condition": list_of_data['current']['condition']['text'],
            "icon": list_of_data['current']['condition']['icon'],
            "humidity": list_of_data['current']['humidity'],
            "wind_speed": f"{list_of_data['current']['wind_kph']} kph",
        }
    except Exception as e:
        data = {"error": "City not found or API error"}

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
