user = input("username : ")
password = input("password : ")
if user == ("toey") and password == ("1234"):
    print("Wellcome Toey")
    print("---100Shop---")
    print("1.Banana      10   Baht")
    print("2.Water        8   Baht")
    print("3.Chocolate   20   Baht")
    print("4.Papsi       12   Baht")
    order = int(input("Order 1-4 : "))
    total = 0
    if 0 < order <= 4:
        if order == 1:
            Banana = int(input("How many Banana do you want ? : "))
            Banana1 = int(10 * Banana)
            print("Total Banana", Banana1, "Baht")
        elif order == 2:
            Water = int(input("How many Water do you want ? : "))
            Water1 = int(8 * Water)
            print("Total Water", Water1, "Baht")
        elif order == 3:
            Chocolate = int(input("How many Chocolate do you want ? : "))
            Chocolate1 = int(20 * Chocolate)
            print("Total Chocolate", Chocolate1, "Baht")
        elif order == 4:
            Papsi = int(input("How many Papsi do you want ? : "))
            Papsi1 = int(12 * Papsi)
            print("Total Papsi", Papsi1, "Baht")
    else:
        print("No Choice")
else:
    print("Login Fail...")