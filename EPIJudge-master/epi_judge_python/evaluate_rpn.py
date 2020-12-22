from test_framework import generic_test
from queue import LifoQueue

def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    intermediate_results = LifoQueue()

    operators = {'+':lambda x, y: x + y, 
                '-' : lambda x, y: y - x,
                '*' : lambda x, y: x * y,
                '/' : lambda x, y: y // x}
    for value in expression.split(','):
        if value in operators:
                intermediate_results.put(operators[value](intermediate_results.get() , intermediate_results.get()))
        else:
            intermediate_results.put(int(value))  

    return intermediate_results.get()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
