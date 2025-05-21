
input_decision = str(
    input("Do you want to sort in Ascending or decending order? (A/D)"))
input_decision = input_decision.lower()


def wrong_check(input_decision):
    while True:
        if (type(input_decision) is not str):
            input_decision = str(
                input("Do you want to sort in ☻Ascending or decending order? (A/D)"))
            input_decision = input_decision.lower()
        else:
            break


wrong_check(input_decision)

while input_decision != "a" and input_decision != "d":
    input_decision = str(
        input("Please enter a valid input(A or D) \n ---->"))
    input_decision = input_decision.lower()


if input_decision == "a":
    input_numbers = str(input("Enter the numbers you want to sort--->"))
    numbers_set = list((input_numbers))

    numbers_set.sort()

    print(numbers_set)
else:
    input_numbers = str(input("Enter the numbers you want to sort--->"))
    numbers_set = list((input_numbers))

    numbers_set.sort()
    numbers_set.reverse()

    print(numbers_set)
