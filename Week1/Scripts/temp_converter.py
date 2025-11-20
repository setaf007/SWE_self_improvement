# conversion functions

from matplotlib.pylab import choice


def celsius_to_fahrenheit(celsius : float) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit : float) -> float:
    return (fahrenheit - 32) * 5/9

# interactive CLI

def main():
    print("Temperature Converter:)")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1/2): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is {f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is {c}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()


