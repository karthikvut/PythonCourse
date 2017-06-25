fruit = {"orange":"a sweet, orange, citrus fruit","apple":"good for making cider","lemon":"a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches","lime":" a sour, green citrus fruit"}

print(fruit)
print(fruit["orange"])
fruit["pear"]="an odd shaped fruit close to apple"
print(fruit)
fruit["apple"]= " a more crunchy fruit"
print(fruit)

del fruit["pear"]
print(fruit)

