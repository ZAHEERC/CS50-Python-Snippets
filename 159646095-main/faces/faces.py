def convert(a):
    if (":)" and ":(") in a:
        x = a.replace(":)", "🙂")
        y = x.replace(":(", "🙁")
        print(y)

    elif ":)" in a:
        x = a.replace(":)", "🙂")
        print(x)

    elif ":(" in a:
        x = a.replace(":(", "🙁")
        print(x)
def main():
    a = input()
    convert(a)

main()
