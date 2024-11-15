a = input("camelCase: ")


for i in a:

    if(i == i.upper()):
        a = a.replace(i, "_" + i.lower())
print("snake_case: " + a)
        