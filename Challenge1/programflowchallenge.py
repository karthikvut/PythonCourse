"""First challenge in Python course"""
ipAddress = input("An IP address consists of 4 sections of numbers separated by . ")
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
#character = ""

for character in ipAddress:
    if character == '.':
        print("segment{0} contains {1} characters".format(segment,segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
