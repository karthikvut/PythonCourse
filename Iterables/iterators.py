list1 = list(["swati", "loves", "karthik", "krishna", "bless", "us"])

list1_iter = iter(list1)

for i in range(0, len(list1)):
    next_item = next(list1_iter)
    print(next_item)
