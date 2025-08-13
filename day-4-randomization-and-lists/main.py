import random

rps_choices = ["Rock", "Paper", "Scissors"]

comp_choice_num = random.randint(1, 3)
comp_choice = rps_choices[comp_choice_num - 1]

human_choice_num = int(input("Select a number between 1 and 3: \n"))
human_choice = rps_choices[human_choice_num - 1]

print(f"The computer chose {comp_choice.lower()} and you chose {human_choice.lower()}")

if human_choice_num == comp_choice_num:
    result = "tie!"
elif (
    (human_choice_num == 1 and comp_choice_num == 3)
    or (human_choice_num == 2 and comp_choice_num == 1)
    or (human_choice_num == 3 and comp_choice_num == 2)
):
    result = "winner!"
else:
    result = "loser!"

print(f"Final result: {result}")
