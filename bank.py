input_str = input("Greeting: ").lower()
if "hello" in input_str:
    print("$0")
elif  input_str[0] == "h":
    print("$20")
else:
    print("$100")