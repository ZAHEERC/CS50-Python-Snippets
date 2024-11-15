a = input("Input: ")
vowels = "aeiouAEIOU"
x = ""
for i in a:
    if i in vowels:
        continue
    x = x + i
print(x)


