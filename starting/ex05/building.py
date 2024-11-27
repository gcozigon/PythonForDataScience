import sys

class TooManyArgs(Exception):
    if len(sys.argv) == 1:
        exit
    else:
        print("TooManyArgs")


def main(args):
    if len(args) != 2:
        raise TooManyArgs()
    upperL = sum(1 for char in args(1) if char.isupper())
    lowerL = sum(1 for char in args(1) if char.islower())
    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punct_total = sum(1 for char in args(1) if char in punct)
    spaces = sum(1 for char in args(1) if char.isspace())
    digits = sum(1 for char in args(1) if char.isdigit())


    print(f"The text contains {len(args[1])} characters:")
    print(f"{upperL} upper letters")
    print(f"{lowerL} lower letters")
    print(f"{punct_total} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except TooManyArgs:
        pass
