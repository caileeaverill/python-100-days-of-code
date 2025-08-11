total_bill = float(input("What is the bill total? \n$"))
num_of_ppl = int(input("How many people?\n"))
tip = int(input("What percent tip? "))

tip_to_percentage = 1 + (tip / 100)
equal_amount = (total_bill / num_of_ppl) * tip_to_percentage

print(f"For everyone to pay an equal amount, you each owe: ${round(equal_amount, 2)}")
