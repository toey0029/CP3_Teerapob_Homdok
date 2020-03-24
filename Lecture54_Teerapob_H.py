def login():
    username = input("Username : ")
    password = input("password : ")
    while username != ("toey") or password != ("1234"):
        if True:
            print("Login Fail...")
            login()
        break
    else:
        print("Wellcome Toey")
        return showMenu()
def showMenu():
    print("---ishop---")
    print("1.Vat Caculator")
    print("2.Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatCalculate(int(input("Price : ")))
    elif userSelected == 2:
        print("Total ", priceCalculate())
def vatCalculate(totalprice):
    result = totalprice + (totalprice * 7 / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product : "))
    return (vatCalculate(price1+price2))
login()