
def menu_taqueria():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    continues = True
    Total = 0
    while continues == True:
        

        try:
            order = input("Item: ")
            if order == "":
                continues = False
            else:
                Total += menu[order]
                print(f"Total: ${Total}")
        except:
            continues = True
menu_taqueria()