import argparse

def calc (x , operation , y):
    match operation:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y


parser = argparse.ArgumentParser()
parser.add_argument('x', type=float)
parser.add_argument('operation', type=str)
parser.add_argument('y', type=float)
args = parser.parse_args()

print(calc(args.x, args.operation, args.y))







