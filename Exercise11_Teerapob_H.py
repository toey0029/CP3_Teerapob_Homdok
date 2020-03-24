number = int(input("Number : "))
for a in range(number):
    star = ""
    for b in range(a*2+1):
        spec = ""
        spec += " "
        star += "*"
    print(spec * (number - a - 1) + star)
