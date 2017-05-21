# ipAddress = input("Please enter an ip address")
# print(ipAddress.count("."))
#
# parrot_list = ["non pinin","no more","a stiff","bereft of live"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is "+ state)
#
# even = [2,4,6,8]
# odd = [1,3,5,7]
#
# numbers = even + odd
# #numbers.sort()
# numbers_in_order = sorted(numbers)
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("Lists are not equal")

# list_1 = []
# list_2 = list()
#
# print("list 1: {0}".format(list_1))
# print("list 2: {0}".format(list_2))
#
# if list_1 == list_2:
#     print("Lists are equal")
#
# print(list("The lists are equal"))

even = [2, 4, 6, 8]
# #another_even = list(even)
# another_even = sorted(even,reverse=True)
# print(another_even is even)
# #another_even.sort(reverse=True)
# print(another_even)
# print(even)

# odd = [1,3,5,7,9]
# numbers = [even,odd]
#
# for number in numbers:
#     print(number)
#
#     for value in number:
#         print(value)

menu = []
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "sausage", "spam"])
menu.append(["egg", "spam"])
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage"])

print(menu)

for meal in menu:
    if not "spam" in meal:
        for item in meal:
            print(item)
