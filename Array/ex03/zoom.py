import os
from load_image import ft_load
import sys
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def ft_zoom():
    print("a")

def main(args):
    try: 
        if not (isinstance(args[0], str) and len(sys.argv) != 3):
            raise Exception("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)
    ft_load(args[1])


if __name__ == "__main__":
    main(sys.argv)