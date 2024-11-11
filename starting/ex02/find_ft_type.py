def all_thing_is_obj(object: any) -> int :
    if (type(object).__name__ == "NoneType") :
         
    else : 
        print(f'{type(object).__name__.capitalize()} : {type(object)}')
    return 42; 
