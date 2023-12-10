from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and ai_choice == "scissors") or
        (user_choice == "paper" and ai_choice == "rock") or
        (user_choice == "scissors" and ai_choice == "paper")
    ):
        return "You win!"
    else:
        return "AI wins!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    ai_choice = get_ai_choice()
    result = determine_winner(user_choice, ai_choice)
    return render_template('result.html', user_choice=user_choice, ai_choice=ai_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)
