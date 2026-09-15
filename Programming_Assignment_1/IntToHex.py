# To use to program, type "python3 IntToHex.py" in the terminal
digits = ['0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

number = int(input("Enter an integer: "))

negative = False
if number < 0:
    negative = True
    number = -number
binary = ""
while number > 0:
    remainder = number % 2
    binary = str(remainder)+binary
    number = number//2

while len(binary) < 32:
    binary = "0" + binary

if negative:
    new_binary = ""

    for bit in binary:
        if bit =="0":
            new_binary = new_binary+"1"
        else:
            new_binary = new_binary+"0"

    binary = new_binary

    carry = 1
    new_binary = ""
    for i in reversed(range(32)):
        bit = int(binary[i]) +carry

        if bit ==2:
            new_binary = "0"+new_binary
            carry = 1
        else:
            new_binary = str(bit)+new_binary
            carry =0
    binary = new_binary

# binary to hexadecimal
hexadecimal = ""

for i in range(0, 32, 4):
    value = 0

    for j in range(4):
        value = value * 2+int(binary[i+j])
    hexadecimal = hexadecimal + digits[value]

print("Binary:", binary)
print("Hex:", hexadecimal)