def coke():
    money_accepted = [5, 10, 25]
    amount_due = 50
    while amount_due > 0:
        print(f"amount due: {amount_due}")
        inserted_money = int(input("Insert coin: "))
        if inserted_money in money_accepted:
            amount_due -= inserted_money
    change_owed = amount_due * -1
    print(f"change owed: {change_owed}")

coke()
