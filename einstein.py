def calculate_percentage(fraction):
    try:
        # Split the fraction into numerator and denominator
        numerator, denominator = map(int, fraction.split('/'))

        # Check if X is greater than Y or Y is 0
        if numerator > denominator or denominator == 0:
            raise ValueError("Invalid fraction. Please try again.")

        # Calculate the percentage
        percentage = (numerator / denominator) * 100

        # Round the percentage to the nearest integer
        rounded_percentage = round(percentage)

        # Check if the tank is essentially empty or full
        if rounded_percentage <= 1:
            return "E"
        elif rounded_percentage >= 99:
            return "F"
        else:
            return f"{rounded_percentage}%"

    except ValueError:
        print("Invalid input. Please enter a valid fraction (X/Y).")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a valid fraction (X/Y).")
        return None


def main():
    continues = True
    while continues == True:
        fraction_input = input("Enter a fraction (X/Y): ")
        result = calculate_percentage(fraction_input)
        
        if result is not None:
            print(result)
            continues = False


main()
