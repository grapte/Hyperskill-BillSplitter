# write your code here
import random


def invite_friends():
    print("Enter the number of friends joining (including you):")
    n = int(input())
    if n <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for i in range(n):
        friends[input()] = 0

    print("Enter the total bill value:")
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'Yes':
        name = random.choice(list(friends.keys()))
        print(f"{name} is the lucky one!")
        for f in friends:
            friends[f] = round(bill / (n-1), 2)
        friends[name] = 0
    else:
        print("No one is going to be lucky")
        for f in friends:
            friends[f] = round(bill / n, 2)

    print(friends)


invite_friends()
