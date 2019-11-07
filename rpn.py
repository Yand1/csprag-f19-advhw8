#!/usr/bin/env python3

import operator
import readline
from colorama import Fore, Style

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
}

def help():
    print("This is a reverse polish notation calculator. It operates by applying" 
          "the operation specified on the two most recent elements, and saving the" 
          "result. Example: 5 6 + becomes 5 + 6, and 11 gets saved to the calculator.")
           

def calculate(arg):
    stack = list()
    for token in arg.split():
        color = Fore.WHITE
        if (token == '+' or token == '-'):
            color = Fore.CYAN
        elif (token == '*' or token == '/'):
            color = Fore.MAGENTA
        elif (token == '^'):
            color = Fore.YELLOW
        print(color + token + Style.RESET_ALL + ' ', end=' ')

        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            try:
                function = operator.__dict__[token]
            except KeyError:
                function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError('malformed input')

    # print(stack[0])

    return stack.pop()    

def main():
    while True:
        result = calculate(input("rpn calc> "))
        
        if result >= 0:
            print(Fore.GREEN)
        else:
            print(Fore.RED)

        print("Result: ", result)

        print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
