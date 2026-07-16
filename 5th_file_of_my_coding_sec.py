import random
import time
print("what while loding the game")
time.sleep(2)
print("====================================")
print("     RANDOM LOOT GENERATOR v1.1     ")
print("====================================")
time.sleep(1)
loot = ["bike(common)" , "airoplane(legendry)" , "car(rare)" , "dimond sword(epic)" , "monster ultra(epic)" , "monster ultra x 24(mythic)"]
inventory = []
while True:
    commands = input("select one of these (open loot / check inventory / exit) : ")
    if commands == "open loot":
        loot_found = random.choice(loot)
        print(f"you get {loot_found}")
        inventory.append(loot_found)
    elif commands == "check inventory":
        if len(inventory) == 0:
            print("your inventory is empty")
        else:
            print("your inventory : ")
            for item in inventory:
                print(item)
    elif commands == "exit":
        print("thanks for playing byyeee")
        break
    else:
        print("invalid choice")