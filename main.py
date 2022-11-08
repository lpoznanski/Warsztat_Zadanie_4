from flask import flask


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