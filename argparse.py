import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argumnet("number1",help="first number")
    parser.add_argumnet("number2",help="second number")
    parser.add_argumnet("operation",help="operation")

    args = parser.parser_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)
