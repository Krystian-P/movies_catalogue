
import requests


def get_movie_library(list_type):
    categories_list = ['now_playing', 'top_rated', 'upcoming', 'popular']
    if list_type in categories_list:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{list_type}?api_key=3d3db789bcf0716515f744cf39623dc2')
    else:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/popular?api_key=3d3db789bcf0716515f744cf39623dc2')
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(list_type, how_many):
    data = get_movie_library(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d3db789bcf0716515f744cf39623dc2&language=en-US')
    return response.json()


def get_backdrop_url(backdrop_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_api_path}"


def get_credits(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3d3db789bcf0716515f744cf39623dc2&language=en-US")
    return response.json()


def get_cast(movie_id, how_many):
    credits = get_credits(movie_id)
    return credits['cast'][:how_many]


def get_movie_images(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=3d3db789bcf0716515f744cf39623dc2&language=en-US")
    return response.json()


