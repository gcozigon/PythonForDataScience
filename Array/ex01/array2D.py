import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integers.")
        

        first_length = len(family[0])
        if any(len(item) != first_length for item in family):
            raise AssertionError("Input list with different sizes.")

        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    
    except AssertionError as e:
        print(f"ERR, {e}")