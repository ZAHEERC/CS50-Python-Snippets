a = input("What is the answer to the Great Question of Life, the Universe and Everything ? ")

a = a.strip()
a = a.lower()
if((a == "42") or (a == "Forty Two") or (a == "forty-two") or (a == "forty two")):
    print("Yes")
else:
    print("No")
