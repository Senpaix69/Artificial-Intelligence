def convertToDec(binary):
    dec = 0
    for i in range(len(binary)):
        dec = (2 ** (len(binary) - 1 - i)) * binary[i] + dec

    return dec

binary = [0, 1, 1]
decimal = convertToDec(binary)
print("Decimal:", decimal)
