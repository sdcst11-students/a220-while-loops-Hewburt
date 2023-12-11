#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
while True:
    entered_number = float(input("Enter number: "))

    if entered_number.is_integer() and int(entered_number) % 2 == 0:
        print("That is an even integer")
        break
    else:
        print("That is not an even integer")
