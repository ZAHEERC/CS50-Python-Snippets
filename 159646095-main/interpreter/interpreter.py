a = input("Expression : ").split()

if "+" in a :
    print(float(int(a[0]) + int(a[2])))
elif "-" in a :
    print(float(int(a[0]) - int(a[2])))
elif "*" in a :
    print(float(int(a[0]) * int(a[2])))
elif "/" in a :
    if(int(a[2]) == 0):
        print("Infinite")
    else:
        x = int(a[0]) / int(a[2])
        print(round(x, 1))
    