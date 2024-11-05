import sys

class TooManyArgs(Exception):
    if len(sys.argv) == 1:
        exit
    else:
        print("TooManyArgs")


def main(args):
    if len(args) != 2:
        raise TooManyArgs()
    upperL = 0
    lowerL = 0
    punct = 0
    spaces = 0
    digits = 0
    for i in args[1]:
        if i.isdigit():
            digits += 1
        elif i.isupper():
            upperL += 1
        elif i.islower():
            lowerL += 1
        elif i.isspace():
            spaces += 1
        else:
            punct += 1

    print(f"The text contains {len(args[1])} characters:")
    print(f"{upperL} upper letters")
    print(f"{lowerL} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except TooManyArgs:
        pass
