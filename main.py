from flask import *


from tmdb_client import *

app = Flask(__name__)

@app.route('/')
def homepage():
    categories_list=['now_playing', 'top_rated', 'upcoming', 'popular']
    selected_list = request.args.get('list_type', "popular")
    movies = get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, categories=categories_list)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = get_single_movie(movie_id)
    cast = get_cast(movie_id, how_many= 4)
    movie_images = get_movie_images(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=movie_images)

@app.errorhandler(404)
def page_not_found(e):
    return('http://127.0.0.1:5000/')


if __name__ == "__main__":
    app.run(debug=True)