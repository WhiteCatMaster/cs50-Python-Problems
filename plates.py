def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    enable = 0
    numbers = False
    able = True
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for letter in s:
        if enable < 2:
            if letter in letters:
                enable += 1
            else:
                able = False
        else:
            if (letter in letters) and (numbers is False):
                enable += 1
            elif (letter in letters) and (numbers is True):
                able = False
            elif letter in number_list:
                enable +=1
                numbers = True
            else:
                able = False
    if enable > 6 or enable < 2:
        able = False
    return able
main()