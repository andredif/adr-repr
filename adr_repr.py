"""
    Module which imitates behaviour of built-in function repr().
    The x_repr function has to be invoked for any-case scenario,
    it starts by recognizing the object type passed as an argument
    of the function, and recursively transforming it and all the nested 
    objects type contained inside in human-readable text.
   """

def repr_int(t: int) -> str:
    """Given an integer, returns the string version of the integer"""
    return str(t)


def repr_tuple(t: tuple) -> str:
    """Given a tuple, starts an iteration on every object of the tuple,
    concatenating the human-readable version of them"""
    str_tuple = '('
    for l in t:
        str_tuple += x_repr(l)
        str_tuple += ', ' if t.index(l)<(len(t)-1) else ''
    return str_tuple+')'    


def repr_list(t: list) -> str:
    """Given a list, starts an iteration on every object of the list,
    concatenating the human-readable version of them"""
    str_list = '['
    for l in t:
        str_list += x_repr(l)
        str_list += ', ' if t.index(l)<(len(t)-1) else ''
    return str_list+']'


def repr_dict(t: dict) -> str:
    """Given a dict, starts an iteration on every object of the dict,
    concatenating the human-readable version of them"""
    str_dict ='{'
    for i,k in enumerate(t.keys()):
        str_dict +=x_repr(k)+': '
        str_dict += x_repr(t.get(k))
        str_dict += ', ' if i<(len(t)-1) else ''
    return str_dict + '}'


def repr_object(t: object) -> str:
    """Given an object,tries to return tre string version of the string;
    if the method is not available for the object type, returns a string 
    containing the class name of the object and his memory id in hexadecimal 
    value, similar but slightly different from the output of repr()"""
    try:
        return str(t)
    except:
        hex_id = hex(id(o))
        return '<'+ t.__class__.__name__ + ' object at ' + str(hex_id)+'>' 


def x_repr(t: object) -> str:
    """This is the entry function for any nested object.It recognizes
    which type is the object and sends it to the other functions of the
    module for transforming in string the nested objects.If the object is as simple
    as an integer or a generic class instance,it returns the string version of it"""
    if isinstance(t, str):
        return t
    elif isinstance(t, int):
        return repr_int(t)
    elif isinstance(t, tuple):
        return repr_tuple(t)
    elif isinstance(t, list):
        return repr_list(t)
    elif isinstance(t, dict):
        return repr_dict(t)
    else:
        return repr_object(t)

    