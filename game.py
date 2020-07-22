# Write your code here
"""import random

# func dec
a = 0
b = 0
c = 0
d = 0


def draw():
    global a
    global b
    global c
    global d
    global name1
    if name1 == 'Tim':
        a += 50
    elif name1 == 'Jane':
        b += 50
    elif name1 == 'Alex':
        c += 50
    else:
        d += 50


def win():
    global a
    global b
    global c
    global d
    global name1
    if name1 == 'Tim':
        a += 100
    elif name1 == 'Jane':
        b += 100
    elif name1 == 'Alex':
        c += 100
    else:
        d += 100


def user_rating():
    global a
    global b
    global c
    global d
    global name1
    if user == '!rating':
        if name1 == 'Tim':
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(a))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
        elif name1 == 'Jane':
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(b))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
        elif name1 == 'Alex':
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(c))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()
        else:
            file = open('rating.txt', 'w')
            file.write('Your rating: {}'.format(d))
            file.close()
            file = open('rating.txt', 'r')
            print(file.read())
            file.close()


# func calling
name = input('Enter your name:')
name1 = name.title()
print(f'Hello,{name1}')
user1 = input()
print('okay, let\'s start')

while True:
    user = input()
    lose_condition = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    rival = ["rock", "paper", "scissors"]
    r_rival = random.choice(rival)
    if user == "!exit":
        print("Bye!")
        break
    elif user == '!rating':
        user_rating()
    elif user not in rival:
        print('Invalid input')
    elif lose_condition[user] == r_rival:
        print('Sorry, but computer chose {}'.format(r_rival))
    elif user == r_rival:
        print('There is a draw ({})'.format(r_rival))
        draw()
    else:
        print('Well done. Computer chose {} and failed'.format(r_rival))
        win()"""
# second
import random


def create_rules(possible_options):
    res = dict.fromkeys(possible_options)

    for i in range(len(res)):
        new_options = possible_options[i + 1:] + possible_options[:i]
        res[possible_options[i]] = new_options[len(new_options) // 2:]

    return res


name = input('Enter your name:')
print(f'Hello, {name}')

with open('rating.txt') as rating:
    score = {line.split()[0]: int(line.split()[1]) for line in rating}.get(name, 0)

symbols = input().split(',')
options = ['rock', 'paper', 'scissors'] if len(symbols) == 1 and symbols[0] == '' else symbols
rules = create_rules(options)

player = input("Okay, let's start\n")

while player != '!exit':
    computer = random.choice(options)

    if player == '!rating':
        print(f'Your rating: {score}')
    elif player not in options:
        print('Invalid input')
    elif player == computer:
        print(f'There is a draw ({computer})')
        score += 50
    elif player in rules[computer]:
        print(f'Sorry, but computer chose {computer}')
    else:
        print(f'Well done. Computer chose {computer} and failed')
        score += 100

    player = input()

print('Bye!')
