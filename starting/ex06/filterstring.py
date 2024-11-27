import sys

def filterstring(args, nb : int):
    try: 
        if not (isinstance(args[0], str) and not isinstance(args[1], int) and len(sys.argv != 3)):
            raise Exception("AssertionError: the arguments are bad")
        text = args[0].split()
        new_text = list(filter(lambda word: len(word) > nb, text))

        print(new_text)
    except AssertionError as e:
        print(e)

def main(args):
    filterstring(args)




if __name__ == "__main__":
        main(sys.argv)
