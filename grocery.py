def main():
    total_orders = {}
    continues = True
    while continues == True:
        order = input("").upper()
        if order == "":
            continues = False
        elif order not in total_orders:
            total_orders[order] = 1
        else:
            total_orders[order] += 1
    for value in total_orders:
        print(f"{total_orders[value]} {value} ")
main()



