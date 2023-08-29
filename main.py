

def fibonacciSequence(num):
    """
    The function generates and prints the Fibonacci sequence up to a given number.
    
    :param num: The parameter "num" represents the number up to which the Fibonacci sequence should be
    generated
    :return: The function does not have a return statement, so it does not return any value.
    """
    if num <= 0:
        print("The number should be positive.")
        return
    
    previous = 0
    next = 1
    result = 0

    print("The fibonacci sequence is: ")
    print(previous, end=", ")
    print(next, end=", ")

    while result < num:
        result = previous + next
        previous = next
        next = result

        print(result, end=", ")


num = int(input("Enter a number: "))
fibonacciSequence(num)