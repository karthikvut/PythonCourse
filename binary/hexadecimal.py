# for i in range(0,17):
#     print("{0:>2} in hexadecimal is {0:>02x}".format(i))
#
#
# x = 0x40
# y = 0x0b
#
# print(x,y)
# print(x * y)
#
# print(0b00110011)

# number = int(input("Enter a number"))
# temp=number
# bin = []

# while temp>=0:
#     if temp < 2:
#         bin.insert(0,temp)
#         if temp == 0:
#             break
#     elif temp % 2 == 0 :
#         bin.insert(0,0)
#     else:
#         bin.insert(0,1)
#     temp = temp//2

powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)

x = int(input("Enter a number"))

printing = False
for power in powers:
    printbit = x // power
    if printbit != 0 or power == 1:
        printing = True
    if printing:
        print(printbit, end="")
    x = x % power
