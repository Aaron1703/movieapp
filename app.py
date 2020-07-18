from flask import Flask, render_template,request
import requests
import imdb
api_address="http://api.openweathermap.org/data/2.5/weather?appid=a1aa80db9de0144444657b76803adfcb&q="
ia = imdb.IMDb()
app=Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/form', methods=['POST'])
def form():
    email = request.form.get('email')
    password=request.form.get('password')
    return render_template("form.html",email=email, password=password)

@app.route('/weather')
def weather():
    return render_template("weather.html")


@app.route('/weather_info', methods=['POST'])
def weather_info():
    city=request.form.get('city')
    url = api_address + city
    json_data = requests.get(url).json()
    weather_data = json_data['weather'][0]['main']
    return render_template("weather_info.html",weather_data=weather_data,city=city)


@app.route('/movies')
def movies():
    return render_template("movies.html")


@app.route('/movies_info', methods=['POST'])
def movies_info():
    movie_name = request.form.get('movie_name')
    print(movie_name)
    movies = ia.search_movie(movie_name)
    print(movies)

    return render_template("movies_info.html",movies=movies)






if __name__=="__main__":
    app.run(debug=True)