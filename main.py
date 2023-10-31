import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

import random
from art import logo

blackjack = 21
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

shouldcontinue = True

def start():
    global shouldcontinue
    while shouldcontinue:
        yourcard = random.sample(cards, 2)
        yourscore = sum(yourcard)

        comcard = random.sample(cards, 2)
        comscore = sum(comcard)

        wannaplay = input("Do you want to play? (yes/no): ").lower()
        if wannaplay == "yes":
            clear()
            if yourscore == blackjack:
                print("You won!")
                break
            else:
                print(logo)
                print("Your current cards:", yourcard, "Current score", yourscore)
                print("Computer's first card:", comcard[0])
                choice = input("Do you wanna get another card? (yes or no): ").lower()

                def cont(choice, yourcard, yourscore, comcard, comscore):
                    if choice == "yes":
                        urnewlist = random.sample(cards, 1)
                        yourcard += urnewlist
                        yourscore += urnewlist[0]
                        print("Your current cards:", yourcard, "Current score", yourscore)
                        print("Computer's first card:", comcard[0])
                        if yourscore == blackjack:
                            print("You won!!")
                            start()
                        elif yourscore > blackjack:
                            print("You lose :( ")
                            start()
                        else:
                            choice = input("Do you wanna get another card? (yes or no): ").lower()
                            cont(choice, yourcard, yourscore, comcard, comscore)
                    else:
                        while comscore < 17:
                            comnewlist = random.sample(cards, 1)
                            comcard += comnewlist
                            comscore += comnewlist[0]
                        print("Your final hand:", yourcard, "Final score", yourscore)
                        print("Computer's final hand:", comcard, "& Final score:", comscore)
                        if comscore == blackjack:
                            print("You lose :(")
                            start()
                        elif comscore > blackjack or comscore < yourscore:
                            print("You won!!")
                            start()
                        else:
                            print("You lose :(")
                            start()

                cont(choice, yourcard, yourscore, comcard, comscore)
        else:
            print("See you next time!")
            shouldcontinue = False

start()
