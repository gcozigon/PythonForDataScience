def all_thing_is_obj(object: any) -> int :
    if (type(object).__name__ == "NoneType") : 
        print("Type Not Found")
        return 
    if (type(object).__name__ == "int") : 
        return 42
    if (type(object).__name__ == "str") : 
        print(f'{object.capitalize()} is in the kitchen : {type(object)}')
        return
    else : 
        print(f'{type(object).__name__.capitalize()} : {type(object)}')
    return 42; 
