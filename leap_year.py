ask_again = True

while ask_again:
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
    elif year % 100 == 0:
        print("Not leap year.")
    else:
        print("Not leap year.")
    question = input("Do you want to check again? Y / N ").lower()
    if question == "y":
        ask_again = True
    elif question == "n":
        print("GoodBye!!")
        ask_again = False
    else:
        print("Invalid Input!!")
        ask_again = False


