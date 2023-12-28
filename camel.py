uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def camel_to_python():
    string = input("camelCase: ")
    str_reset = ""
    for letter in string:
        if letter in uppers:
            str_reset += "_" + letter.lower()
        else:
            str_reset += letter
    print(f"snake_case: {str_reset}")
camel_to_python()