binary = input("Enter a binary number: ")

# Validate input
if not all(bit in '01' for bit in binary):
    print("Invalid binary number. Please enter a valid binary string.")
else:
    decimal = 0
    for i in binary:
        decimal = decimal * 2 + int(i)
    print("The decimal equivalent is:", decimal)
