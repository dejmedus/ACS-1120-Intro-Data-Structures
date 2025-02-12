"""Main script, uses other modules to generate sentences."""
from flask import Flask
import random
from dictogram import Dictogram
from rearrange import rearrange

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    words = ["apple", "banana", "cherry", "date", "elderberry",
             "fig", "grape", "honeydew", "kiwi", "lemon"]
    dictogram = Dictogram(words)

    items_list = list(dictogram.items())
    random_sample = random.sample(items_list, min(5, len(items_list)))
    words_list = [word for word, freq in random_sample]
    sentence = rearrange(words_list)

    # """Route that returns a web page containing the generated text."""
    return f"<p>{sentence}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
