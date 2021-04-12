from flask import (Flask, request, render_template, redirect, session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "LeggoMyEggo"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



boggle_game = Boggle()

@app.route('/')
def load_game():
    """Loads boggle game and board."""
    boggle_board = boggle_game.make_board()
    session['board'] = boggle_board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template('home.html', board=boggle_board, highscore=highscore,
                           nplays=nplays)


@app.route("/check-word")
def check_word():
    """Check if word is in dictionary."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})


@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)