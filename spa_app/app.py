from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["stone", "paper", "scissor"]

@app.route("/", methods=["GET", "POST"])
def home():

    user_choice = ""
    computer_choice = ""
    result = ""

    if request.method == "POST":
        user_choice = request.form.get("choice")
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "🤝 Tie"

        elif (
            (user_choice == "stone" and computer_choice == "scissor") or
            (user_choice == "scissor" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "stone")
        ):
            result = "🎉 You Win"
        else:
            result = "🤖 Computer Wins"

    return render_template("index.html",
                           user=user_choice,
                           computer=computer_choice,
                           result=result)

if __name__ == "__main__":
    app.run(debug=True)