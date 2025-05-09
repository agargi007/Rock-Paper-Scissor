from flask import Flask, render_template, request
import random

app = Flask(__name__)

CHOICES = ['rock', 'paper', 'scissors']

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_choice = None
    computer_choice = None
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(CHOICES)
        result = get_winner(user_choice, computer_choice)
    return render_template('index.html',
                           result=result,
                           user_choice=user_choice,
                           computer_choice=computer_choice)

if __name__ == '__main__':
    app.run(debug=True)
