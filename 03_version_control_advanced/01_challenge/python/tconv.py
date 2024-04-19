def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")

def convert_fahrenheit_to_celsius():
    print("Enter the temperature in Fahrenheit:")
    F = input()
    F = int(F)
    C = 5/9 * (F - 32)
    print(f"The Fahrenheit temperature {F} you entered is {C} in Celsius.")

def main():
  convert_fahrenheit_to_celsius()
  convert_celsius_to_fahrenheit()
 

main()