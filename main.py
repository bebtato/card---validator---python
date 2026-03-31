"""
Robert Castro 
""" 
# imports maths
import math


def errorcheck(cardNumber):
    # cheacks if the card number is between 13 and 16 numbers long
    if not (13 <= len(cardNumber) <= 16):
        print(f"Credit Card Number {cardNumber} is invalid.")
        return False

    # check for correct card starting number
    if cardNumber.startswith(("4", "5", "37", "6")):
        return True

    else:
        print(f"Credit Card Number {cardNumber} is invalid.")
        return False


# formula to finds the total of the even digits
def sumOfDoubleEvenPlace(number):
    sum_even_num = 0
    # reads right to left
    for i in str(number)[-2::-2]:
        double_value = int(i) * 2
        if double_value >= 10:
            sum_even_num += double_value - 9
        else:
            sum_even_num += double_value

    return sum_even_num


# formula to finds the total of the odd digits
def sumOfOddPlace(number):
    sum_odd_num = 0
    # read right to left
    for n in str(number)[-1::-2]:
        sum_odd_num += int(n)

    return sum_odd_num


def main():
    # opens the input file loop
    with open("input.dat", "r") as file:
        for cardNumber in file:
            cardNumber = cardNumber.strip()

            # starts errorcheck function
            if errorcheck(cardNumber):

                # gets values from the two functions odd and evem
                sum_odd_num = sumOfOddPlace(cardNumber)
                sum_even_num = sumOfDoubleEvenPlace(cardNumber)

                total = sum_odd_num + sum_even_num

                if total % 10 == 0:
                    print(f"Credit Card Number {cardNumber} is valid")
                else:
                    print(f"Credit Card Number {cardNumber} is invalid")


if __name__ == "__main__":
    main()
