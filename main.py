"""
Robert Castro 

Problem

Credit Card Validation

Credit card numbers follow certain patterns. It must have between 13 and 16 digits, and
the number must start with:
 4 for Visa cards
 5 for MasterCard cards
 37 for American Express cards
 6 for Discover cards

In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers.
The algorithm is useful to determine whether a card number is entered correctly or
whether a credit card is scanned correctly by a scanner. Credit card numbers are
generated following this validity check, commonly known as the Luhn check or the Mod
10 check, which can be described as follows (for illustration, consider the card number
4388576018402626):

1. Double every second digit from right to left. If doubling of a digit results in a two-digit
number, add up the two digits to get a single-digit number.

Picture

2. Now add all single-digit numbers from Step 1.

4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

3. Add all digits in the odd places from right to left in the card number.

6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

4. Sum the results from Steps 2 and 3.

37 + 38 = 75

5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is
invalid. For example, the number 4388576018402626 is invalid.

Example: 4388576018410707

1. Double every second digit from right to left. If doubling of a digit results in a two-digit
number, add up the two digits to get a single-digit number.

(0 * 2) + (0 * 2) + (4 * 2) + (1 * 2) + (6 * 2) + (5 * 2) + (8 * 2) + (4 * 2)
0 + 0 + 8 + 2 + 3 + 1 + 7 + 8 = 29

2. Now add all single-digit numbers from Step 1.

0 + 0 + 8 + 2 + 3 + 1 + 7 + 8 = 29

3. Add all digits in the odd places from right to left in the card number.

7 + 7 + 1 + 8 + 0 + 7 + 8 + 3 = 41

4. Sum the results from Steps 2 and 3.

29 + 41 = 70

5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is
invalid. For example, the number 4388576018410707is valid.

Algorithm:
1. Check if the input string has >=13 and <=16 characters. If false, then invalid card
number, else Step 2.
2. Check if the input string begins with 4, 5, 37, or 6. If false, then invalid card number,
else Step 3.
3. Perform Steps 1 & 2 from above. Call the method below and return the result:
            def sumOfDoubleEvenPlace (number):

4. Perform Step 3 from above. Call the method below and return the result:
            def sumOfOddPlace (number):
            
5. Perform Steps 4 & 5 from above. Determine if valid or invalid.

Add any other functions you think are necessary.

Write a program that reads from an input file N credit card numbers. Display whether
the numbers are valid or invalid. Do not check for invalid input. All input strings will
contain only digits.

Sample Input File:
4388576018
4388576018402626
4388576018410707
43885760184107074
584638594017483
378282246310005
378282246310006
6011000990139424
6011000890139424
5105105105105100
5105104105105100
51051051051051005
510510
510510505105

Sample Output:
Credit Card Number 4388576018 is invalid
Credit Card Number 4388576018402626 is invalid
Credit Card Number 4388576018410707 is valid
Credit Card Number 43885760184107074 is invalid
Credit Card Number 584638594017483 is invalid
Credit Card Number 378282246310005 is valid
Credit Card Number 378282246310006 is invalid
Credit Card Number 6011000990139424 is valid
Credit Card Number 6011000890139424 is invalid
Credit Card Number 5105105105105100 is valid
Credit Card Number 5105104105105100 is invalid
Credit Card Number 51051051051051005 is invalid
Credit Card Number 510510 is invalid

Credit Card Number 510510505105 is invalid
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
