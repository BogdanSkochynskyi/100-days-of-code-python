from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = int(input("Enter the first number: "))
continue_with_calculation = True
while continue_with_calculation:
    operator = input("Enter the operator: \n+\n-\n*\n/\n")

    second_number = int(input("Enter the second number: "))

    result = operations[operator](first_number, second_number)
    print(f"{first_number} {operator} {second_number} = {result}")
    continue_with_calculation = input("Do you want to continue? (y/n): ")
    if continue_with_calculation == "n":
        continue_with_calculation = False
    else:
        first_number = result
