from random import choice


def outcome():  # returns who's won
    play = options.index(player)
    
    new_list = options[play:] + options[:play]
    com = new_list.index(computer)
    middle = len(new_list) // 2

    if computer == player:
        return "tie"
    
    elif middle < com:
        return "computer"
    
    else:
        return "player"


def output():  # prints match outcome
    if winner == "tie":
        print(f"There is a draw ({computer})")
        scores[name] += 50

    elif winner == "player":
        print(f"Well done. The computer chose {computer} and failed")
        scores[name] += 100

    else:
        print(f"Sorry, but the computer chose {computer}")


def rating():  # prints the users rating
    print(scores[name])


scores = {}  # a dictionary for everyones ratings

with open("rating.txt", "r") as file:  # puts everyones scores into the dictionary
    for line in file:
        key, value = line.strip().split()
        value = int(value)
        scores[key] = value


name = input("Enter your name: ")  # get's the users name
print(f"Hello, {name}")

op = input()  # lets the user choice the options
if op:
    options = list(op.split(","))
else:
    options = ["scissors", "paper", "rock"]  # if nothing is entered goes to default

print("Okay, let's start")

if name not in scores:  # if name isn't in dictionary it is added
    scores[name] = 0

while True:  # runs the game
    computer = choice(options)  # get's the computers choice
    player = input()  # get's the users choice

    if player == "!exit":  # ends the game
        break
    
    elif player == "!score":  # prints the users rating
        rating()

    elif player not in options:  # if the user enters an invalid option
        print("Invalid input")
    else:
        winner = outcome()
        output()

print("Bye!")

with open("rating.txt", "w") as file:  # puts everyones new scores into the file
    for person in scores:
        file.writelines(person + " " + str(scores[person]) + "\n")
