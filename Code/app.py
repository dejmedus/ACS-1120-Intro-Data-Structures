"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from random import choice

from utils.tokens import tokenize
from utils.markov import MarkovChain


DATA = 'data/corpus.txt'
# removed words 'This', 'The', 'At', 'An', 'A', 'You', 'When', 'Your', 'Arcs', 'Positive', 'Bane', 'Primal', 'Infuse'
IN_WORDS = ['Creates', 'Flames', 'Reduces', 'Blasts', 'Gives', 'Cures', 'Delivers', 'Wards', 'Imbues', 'Damages', 'Gestures', 'Allows', 'Instills', 'Harnesses', 'Increases',
            'Transmutes', 'Summons', 'Grants', 'Charms', 'Induces', 'Fires', 'Conjures', 'Enchants', 'Telekinetically', 'Covers', 'Makes', 'Enemies']

app = Flask(__name__)
source = open(DATA).read()
tokens = tokenize(source)
chain = MarkovChain(tokens)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    start_word = choice(IN_WORDS)
    spell = chain.random_walk(start_word)

    return render_template('index.html', spell=spell)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
