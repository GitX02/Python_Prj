import random

choose_num=input("Choose a number from 1 to 100")
pick_num=random.randrange(1,100)
if pick_num==choose_num:
    print("Lucky winner! The number picked from draw is ",pick_num)
else:
    print("Try again")

