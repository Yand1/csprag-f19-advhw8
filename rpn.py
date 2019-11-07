#!/usr/bin/env python3

import operator

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

    print(stack[0])

    return stack.pop()    

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
