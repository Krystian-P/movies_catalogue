from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
    movies=['elo', '320', 'XD']
    return render_template("homepage.html", movies = movies)

if __name__ == "__main__":
    app.run(debug=True)