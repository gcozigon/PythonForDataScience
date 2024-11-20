from PIL import Image
import numpy as np


def ft_load(path: str)  -> np.ndarray:
    im = Image.open(f'{path}')
    rgb_im = im.convert('RGB')
    rgb_array = np.array(rgb_im)
    
    print(f"The shape of image is: {rgb_array.shape}")
    
    return rgb_array
