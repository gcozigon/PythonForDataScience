from PIL import Image
import numpy as np
import os


def ft_load(path: str)  -> np.ndarray:
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        im = Image.open(f'{path}')
        rgb_im = im.convert('RGB')
        rgb_array = np.array(rgb_im)

        print(f"The shape of image is: {rgb_array.shape}")

        return rgb_array
    except AssertionError as e:
        print(f"{e}")
        return ""
