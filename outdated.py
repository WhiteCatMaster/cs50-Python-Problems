def main():

    continues = True
    while continues == True:
        try:
            date = input("Date:")
            date_1 = date.split("/")
            date_2 = date.split("; ").split(" ")
            print(date_1)
            if len(date_1) == 3:
                if (int(date_1[0]) <= 31) and (int(date_1[1]) <= 12):
                    print(f"{date_1[2]}-{date_1[1]}-{date_1[0]}")
                    continues = False
                else:
                    pass
            else:
                if len(date_2) == 3:
                    if (int(date_2[0]) <= 31) and (months_to_number(date_2[1]) <= 12):
                        print(f"{date_2[2]}-{months_to_number(date_2[1])}-{date_1[0]}")
                        continues = False
                else:
                    pass
        except:
            pass
            
def months_to_number(month_to_pass):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    count = 0
    for month in months:
        count += 1
        if month == month_to_pass:
            return count
        else:
            pass





            

    
main()