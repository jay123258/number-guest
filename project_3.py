import random

a = random.randint(1,100)

b = 0


while True:
    user = int(input("enter your number: "))


    if user<a:
        print("enter your higher number: ")

    elif user>a:
        print("enter your lawer number: ")

    else:
        print(f"your choice is {a}")