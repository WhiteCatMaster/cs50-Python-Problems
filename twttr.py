def main():
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    input_name = input("input: ")
    output_name = ""
    for letter in input_name:
        if letter not in vowels:
            output_name += letter
    return (f"output: {output_name}")
print(main())
