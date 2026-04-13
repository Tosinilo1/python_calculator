while True:
    print("Simple calculator")
    
    num1 = float(input("Enter first number:"))
    
    operator = input("Enter operator (+, -, *, /):").strip()
    
    num2 = float(input("Enter second number:"))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Divison by zero."
    else:
            result = "Invalid operator"

    print("Result:", result)
    
    again = input("Do you want to continue? (y/n):")
    
    if again.lower() != "y":
        
            break
        
