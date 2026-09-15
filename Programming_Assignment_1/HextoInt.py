# To use to program, type "python3 HextoInt.py" in the terminal
digits = ['0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

hexadecimal = input("Enter a 32-bit hexadecimal number: ")
number = 0
for digit in hexadecimal:
    if digit == '0':
        value = 0
    elif digit == '1':
        value = 1
    elif digit == '2':
        value = 2
    elif digit == '3':
        value = 3
    elif digit == '4':
        value = 4
    elif digit == '5':
        value = 5
    elif digit == '6':
        value = 6
    elif digit == '7':
        value = 7
    elif digit == '8':
        value = 8
    elif digit == '9':
        value = 9
    elif digit == 'A':
        value = 10
    elif digit == 'B':
        value = 11
    elif digit == 'C':
        value = 12
    elif digit == 'D':
        value = 13
    elif digit == 'E':
        value = 14
    elif digit == 'F':
        value = 15

    number = number * 16 + value

print("Decimal:", number)
