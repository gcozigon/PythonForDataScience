def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print("Type of None:", type(object))
        elif isinstance(object, float) and object != object:
            print("Type of NaN:", type(object))
        elif object == 0:
            print("Type of Zero:", type(object))
        elif object == '':
            print("Type of Empty string:", type(object))
        elif object is False:
            print("Type of False:", type(object))
        else:
            raise Exception("Type not Found")
        return 0
    except Exception as e:
        print(e)
        return 1
