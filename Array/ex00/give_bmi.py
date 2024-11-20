def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight values must be int or float.")
        if h <= 0:
            raise ValueError("Height must be a positive number.")
        
        bmi = w / (h ** 2)
        bmi_list.append(bmi)

    return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI values must be int or float.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    return [b > limit for b in bmi]