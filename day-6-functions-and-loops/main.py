import random
import time

treasure_coords = []
current_coords = [0, 0]

for _ in range(2):
    random_coord = random.randint(0, 10)
    treasure_coords.append(random_coord)


print(f"Treasure located at: {treasure_coords}")


def locate_treasure_x():
    while not current_coords[0] == treasure_coords[0]:
        current_coords[0] += 1
    else:
        print(f"Beep beep! The treasure is located at X: {current_coords[0]}")


def locate_treasure_y():
    while not current_coords[1] == treasure_coords[1]:
        current_coords[1] += 1
    else:
        print(f"Beep beep! The treasure is located at Y: {current_coords[1]}")


def treasure_location():
    print(f"The treasure is located at: {current_coords[0]}, {current_coords[1]}")


while not treasure_coords == current_coords:
    print("No treasured buried here. Searching for treasure.")
    time.sleep(0.6)
    for i in range(10):
        print("...")
        time.sleep(0.8)

    locate_treasure_x()
    locate_treasure_y()
else:
    treasure_location()
