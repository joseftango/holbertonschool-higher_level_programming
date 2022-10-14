#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

arg_num = len(argv[1:])

if arg_num != 3:
    print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

operator = argv[2]

if operator == '+':
    use = add
elif operator == '-':
    use = sub
elif operator == '*':
    use = mul
elif operator == '/':
    use = div
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(argv[1])
b = int(argv[3])

res = use(a, b)

print(f"{a} {operator} {b} = {res}")
