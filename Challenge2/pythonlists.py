menu = []
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "sausage", "spam"])
menu.append(["egg", "spam"])
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage"])
menu.append(["egg", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])

print(menu)

for meal in menu:
    if not "spam" in meal:
        for item in meal:
            print(item)
