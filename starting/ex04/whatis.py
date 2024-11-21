import sys

class MoreThanOneArgumentError(Exception):
    pass

class NotAnIntegerError(Exception):
    pass

def main(args):
    if len(args) > 2:
        raise MoreThanOneArgumentError("AssertionError: more than one argument is provided")
    
    if len(args) == 2:
        try:
            number = int(args[1])
            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise NotAnIntegerError("AssertionError: argument is not an integer")
    else:
        print("No arguments received.")

if __name__ == "__main__":
    try:
        main(sys.argv)
    except MoreThanOneArgumentError as e:
        print(e)
    except NotAnIntegerError as e:
        print(e)
