import sys

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


class MoreThanOneArgumentError(Exception):
    pass

class ErrChar(Exception):
    pass

def main(args):
    if len(args) != 2:
        raise MoreThanOneArgumentError("AssertionError: more than one argument is provided")
    for i in args[1].upper():
        if i in morse_code_dict:
            print(morse_code_dict[i], end=' ')
        else:
            raise ErrChar("AssertionError: the arguments are bad")
    print()

if __name__ == "__main__":
    try:
        main(sys.argv)
    except MoreThanOneArgumentError as e:
        print(e)
    except ErrChar as e:
        print(e) 