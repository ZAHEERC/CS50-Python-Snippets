month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        m, d, y = date.split('/')
        m = int(m) # which means that if 'm' is a string it will produce ValueError
    except ValueError:
        pass
    else:
        if int(d)<32 and m < 13:
            print(f"{y.zfill(4)}-{m:02}-{d.zfill(2)}", end="")
            break

    try:
        temp1, y = date.split(', ')
        m, d = temp1.split()
        m = str((month.index(m))+1) #if 'm' is not in the list "month" then it will producde a KeyError
    except (ValueError, KeyError):
        pass
    else:
        if int(d) < 32 and int(m) < 13:
            print(f"{y.rjust(4, '0')}-{m.rjust(2, '0')}-{d.rjust(2, '0')}", end="")
            break




