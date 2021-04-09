from flask import (Flask, request, render_template, redirect, flash, session)
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, Question, satisfaction_survey, surveys

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "LeggoMyEggo"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

from boggle import Boggle

boggle_game = Boggle()

@app.route('/')
def load_boggle():
    """Loads boggle game and board."""

    return render_template('home.html')