# Exceptional Weather Forecast

def convert_to_celsius():
    while True:
        try:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            c = (fahrenheit - 32) * 5 / 9
            celsius = round(c, 1)
        # I know the example output on the instructions had two decimal places, but I think it looks much nicer
        # just to have one. Let me know if that's unacceptable, and I will change it to two.
        except ValueError:
            print("That's not a valid value. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred. Details: {e}")
        else:
            print(str(fahrenheit), "degrees Fahrenheit is equal to", celsius, "degrees Celsius.")
        finally:
            print("Thanks for using my Fahrenheit to Celsius converter.")
            break


convert_to_celsius()