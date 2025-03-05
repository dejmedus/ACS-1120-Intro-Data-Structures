"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template

from utils.tokens import tokenize
from utils.markov_higher_order import MarkovChain

DATA = 'data/dungeons-and-dragons.txt'

app = Flask(__name__)
source = open(DATA).read()
tokens = tokenize(source)
chain = MarkovChain(tokens, 2)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""

    spell = chain.random_walk()

    return render_template('index.html', spell=spell)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
