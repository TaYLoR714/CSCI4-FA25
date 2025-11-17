#python
import array as array

def addition(num1: int, num2: int) -> None:
    print(num1 + num2)

def subtraction(num1: int, num2: int) -> None:
    print(num1 - num2)

def multiplication(num1: int, num2: int) -> None:
    print(num1 * num2)

def division(num1: int, num2: int) -> None:
    if num2 == 0:
        raise ValueError

    print(num1 / num2)


    #------------------------------------

    operator = input("Enter and operator(+-*/): ")
    num1 = input("enter the first number: ")
    num2 = input("enter the second number: ")