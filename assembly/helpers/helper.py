def is_constant_name(name): #check if variable has the naming convention of starting with a '_' followed by uppercase letters
    if name[0] != '_':
        return False
    for i in range(1, len(name)):
        if not name[i].isupper():
            return False
    return True