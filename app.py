from flask import Flask, render_template, request
import requests
app = Flask(__name__)
from matplotlib import pyplot as plt
from datetime import datetime as dt
@app.route('/')
def search():
    return render_template('home.html')


@app.route('/results', methods=["GET", "POST"])
def results():
    api_key = "4ccc7cabc4bac53437084c5a6f2e1781"
    city = request.form.get('city')
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    print(url)
    response = requests.get(url).json()
    location = response.get("name")
    timezone = response.get("timezone")
    timestamp = response.get("dt")
    date_time = dt.fromtimestamp(timestamp )
    local_timestamp = ""
    temp_k = response.get("main").get("temp")
    print(temp_k)
    temp_c = temp_k - 273.15
    description = ""
    wind_speed = response.get("wind").get("speed")
    iconcode = response.get("weather")[0].get("icon")
    print(iconcode)
    icon_url = "http://openweathermap.org/img/w/" + iconcode + ".png"
    print(icon_url)
    my_list = [response, location, timezone, timestamp, date_time, local_timestamp, temp_k, temp_c, description, wind_speed, icon_url]
    print(response)
    x_time= [0, 1, 2, 3, 4, 5, 6]
    y_temp= [18, 15, 13, 10, 8, 13, 18]
    plt.plot(x_time, y_temp )
    plt.savefig("testplot")

    return render_template('results.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)




















































































