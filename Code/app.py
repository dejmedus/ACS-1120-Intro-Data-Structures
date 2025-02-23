"""Main script, uses other modules to generate sentences."""
from flask import Flask
from random import randrange

from utils.tokens import tokenize
from utils.markov import MarkovChain


DATA = 'data/corpus.txt'

app = Flask(__name__)
source = open(DATA).read()
tokens = tokenize(source)
chain = MarkovChain(tokens)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    start_index = randrange(len(tokens))
    start_word = tokens[start_index]
    sentence = chain.random_walk(start_word)

    return f"<h2>{sentence}</h2>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
