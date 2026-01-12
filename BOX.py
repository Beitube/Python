n = int(input())

binary = bin(n)[2:]
octal = oct(n)[2:]
hexa = hex(n)[2:].upper()

print(binary, octal, hexa, sep = "\n")
