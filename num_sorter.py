
input_decision = str(
    input("Do you want to sort in Ascending or decending order? (A/D)"))
input_decision = input_decision.lower()

if input_decision == "a":
    input_numbers = str(input("Enter the numbers you want to sort--->"))
    numbers_set = list((input_numbers))

    numbers_set.sort()

    print(numbers_set)
elif input_decision == "d":
    input_numbers = str(input("Enter the numbers you want to sort--->"))
    numbers_set = list((input_numbers))

    numbers_set.sort()
    numbers_set.reverse()

    print(numbers_set)
else:
    print("Please select between only A or D")
