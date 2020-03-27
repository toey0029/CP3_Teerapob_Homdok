menuList = []
priceList = []
def showBill():
    print("My Food")
    totalprice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalprice += int(priceList[number])
    print("Total : ",totalprice)
while True:
    menuName = input("Enter your menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(int(menuPrice))
showBill()

