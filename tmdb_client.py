import requests


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDNkYjc4OWJjZjA3MTY1MTVmNzQ0Y2YzOTYyM2RjMiIsInN1YiI6IjYwY2EyZjRjYjBiYTdlMDAzZjVlMDlmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.WX8NDQUu747jGFpWHEU2ltIRyxk0DgoXDuZzTP-1K78"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movie_library(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_poster_url(poster_api_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(list_type, how_many):
    data = get_movie_library(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d3db789bcf0716515f744cf39623dc2&language=en-US')
    return response.json()


def get_backdrop_url(backdrop_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_api_path}"


def get_credits(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3d3db789bcf0716515f744cf39623dc2&language=en-US")
    return response.json()


def get_cast(movie_id, how_many):
    credits = get_credits(movie_id)
    return credits['cast'][:how_many]


def get_movie_images(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=3d3db789bcf0716515f744cf39623dc2&language=en-US")
    return response.json()
