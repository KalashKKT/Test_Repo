import random

Comp=0
user=0
S="Snake"
W="Water"
G="Gun"

name=input("Type your name: ")
round=int(input("How many rounds you want to play? "))
print("Snake-S","Water-W","Gun-G")

while round>0:
    options=["S","W","G"]
    player=input("Choose any one from Above: ")
    computer=random.choice(options)

    if computer=='S':
        if player=='G':
            user=user+1
            print(f"{name} wins: {user}  Comp wins: {Comp} ")
        elif player=='W':
            Comp=Comp+1
            print(f"Comp wins: {Comp}   {name} wins: {user} ")

    elif computer=='W':
        if player=='S':
            user=user+1
            print(f"{name} wins: {user}  Comp wins: {Comp}")
        elif player=='G':
            Comp=Comp+1
            print(f"Comp wins: {Comp}  {name} wins: {user}")

    elif computer=='G':
        if player=='W':
            user=user+1
            print(f"{name} wins: {user}  Comp wins: {Comp}")
        elif player=='S':
            Comp=Comp+1
            print(f"Comp wins: {Comp}  {name} wins: {user}")
    round=round-1
