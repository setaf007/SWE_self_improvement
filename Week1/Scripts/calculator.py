def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple python calculator\nSelect Operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        match choice:
            case '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            case '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            case '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            case '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() == 'yes':
            continue
        elif next_calculation.lower() == 'no':
            break
        else:
            print("Invalid Input")
            break
    else:
        print("Invalid Input")
