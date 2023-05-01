#Import environment variables (SPOTIPY KEYS)
from dotenv import load_dotenv
load_dotenv()

from flask import render_template, json, url_for
from main import app
# from app import app
from recommendations import get_recommendations, get_covers, display
from forms import SearchForm


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():

    form = SearchForm()

    if form.validate_on_submit():

        recommendations = get_recommendations(form.search.data)
        covers = get_covers(recommendations)
        html_code = display(recommendations, covers)


        return render_template('index.html', title = 'Beats - Song Recommender Engine', \
            form = form, html_code = html_code)

    return render_template('index.html', title = 'Beats - Song Recommender Engine', form = form)

app.run(debug=True)