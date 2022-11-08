from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def game():
    min = 0
    max = 1000
    guess = int((max - min) / 2) + min

    if request.method == "POST":
        answer = request.form["button"]
        if answer == "3":
            return "Hooray! I won!"
        elif answer == "2":
            max = guess
            guess = int((max - min) / 2) + min
            return render_template("index.html", guess=guess)
        else:
            min = guess
            guess = int((max - min) / 2) + min
            return render_template("index.html", guess=guess)
    else:
        return render_template("index.html", guess=guess)




        # else:
        #     return render_template("index.html", guess=guess)
# def form():
#     min = 0
#     max = 1000
#     guess = int((max - min) / 2) + min

#
#
#     html = """
#     <html>
#         <h1>Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max 10 próbach</h1>
#         </br>
#         <form action="/" method="POST">
#             <label>
#             Zgaduję: {{ guess }}
#             </label>
#             </br>
#             </br>
#             <button type="submit">Not enough</button>
#             <button type="submit">Too much</button>
#             <button type="submit">You win!</button>
#         </form>
#     </html>
#     """
#
#
#
#
    # if request.method == "POST":
    #     answer = request.form["answer"]
    #         if answer == "You win!":
    #             print("Wygrałeś!")
    #
    #         elif answer == "za dużo":
    #             max = guess
    #         elif answer == "za mało":
    #             min = guess
    #         else:
    #             print("nie oszukuj!")

    # return html

if __name__ == "__main__":
    app.run(debug=True, port=5000)


# print("""
# Pomyśl liczbę od 0 do 1000,
# a ja ją zgadnę w max 10 próbach
# """)
# min = 0
# max = 1000
# while True:
#     guess = int((max - min) / 2) + min
#     print(f"Zgaduję: {guess}")
#     answer = input("""Wpisz
#   za dużo
#   za mało
#   lub zgadłeś
#   :""")
#     if answer == "zgadłeś":
#         print("Wygrałem!")
#         break
#     elif answer == "za dużo":
#         max = guess
#     elif answer == "za mało":
#         min = guess
#     else:
#         print("nie oszukuj!")