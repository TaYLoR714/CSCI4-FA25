#python CALCULATOR HOMEWORK TURNIN
import array as array

def evaluate(x, y, o):
    """
    Performs a calculator function on x and y based on the operator o.
    """
    
    # Detect what operation is used using the "o" variable
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        # Handle when you divide by 0
        if y == 0:
            print(f"Error: Cannot divide {x} by zero.")
            return None
        return x / y
    else:
        # Handle any other unknown operation
        print(f"Error: Unknown operation '{o}'.")
        return None


print("Running Calculator Tests")

# (x, y, operation)
test_cases = [
    (5, 5, '+'),    # 1.| 5 + 5
    (1, -1, '+'),   # 2.| 1 + (-1)
    (0, -1, '-'),   # 3.| 0 - (-1)
    (0, 5, '/'),    # 4.| 0 / 5
    (4, 2, '/'),    # 5.| 4 / 2
    (2, 1, '*'),    # 6.| 2 * 1
    (3, 2, '*')     # 7.| 3 * 2
]
# Getting the calclator to work using the test cases from the assignment
for test in test_cases:

    x, y, o = test
    
    print(f"Calculating: {x} {o} {y}")
    
    # Get the result from the function
    result = evaluate(x, y, o)
    
    # Print the result if it's valid
    if result is not None:
        print(f"Answer: {result}")
    

print("Ending Calculator Tests")