from flask import Flask

app = Flask(__name__)


def generate_random_number():
    from random import randint
    return randint(0, 9)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<h3>Enter your number in the URL.</h3>' \
           '<h4>example: http://127.0.0.1:5000/4</h4>' \
           '<img src="https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif">'


@app.route("/<int:your_number>")
def check_number(your_number):
    random_number = generate_random_number()
    if your_number < random_number:
        return "<h1>Too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif your_number > random_number:
        return "<h1>Too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1>You got it</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)

