print("You arrive at a crossroad on Treasure Island.")
direction = (
    input("Do you go left into the shadowy forest, or right toward the cliffs?\n")
    .strip()
    .lower()
)

if direction == "left":
    action = input("Swim or wait?\n").strip().lower()
    if action == "swim":
        door = input("Red, blue or yellow door?\n").strip().lower()
        if door == "red":
            print("Burned by fire. Game over. ")
        elif door == "blue":
            print("Eaten by beasts. Game over. ")
        elif door == "yellow":
            print("You cleared the island! You win!")
        else:
            print("Game over.")
    else:
        print("Attacked by trolls. Game Over.")
else:
    print("Fall into a hole. Game Over.")
