a = input("Greeting : ")
a = a.strip().lower()

if(a.startswith("h")):
    if(a.startswith("hello")):
        print("$0")
    else:
        print("$20")
else:
    print("$100")

