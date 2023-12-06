def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "The denominator can't be 0 ! "
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    global answer
    should_continue = True

    n1 = float(input("What's the first number? "))
    while should_continue:
        n2 = float(input("What's the second number? "))
        for symbols in operators:
            print(symbols)
        symbol = input("Which of the above operations do you want to apply? ")
        calculation_func = operators[symbol]
        answer = calculation_func(n1, n2)

        if input(f"Type y to continue calculating with {answer}, type n to start a new calculation. ") == 'y':
            n1 = answer

        else:
            should_continue = False
            calculator()

    print(answer)


calculator()
