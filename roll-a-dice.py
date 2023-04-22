import random
resp = "y"
resp = input("Do you want to roll a dice? (y/n): ")


while resp == "y":
    no = str(random.randint(1,6))
    print("[ ---- ]")
    print("["+no,"   "+no+"]")
    print('[ ',no,'  ]')
    print("["+no,"  "+no+" ]")
    print("[ ---- ]")

    resp = input("Do you want to roll a dice? (y/n): ")
while resp == "n":
    break


