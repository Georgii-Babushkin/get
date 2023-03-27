def to_list(_str):
    lst = _str.split()
    lst.sort(key = len)
    return(len(lst[-1]))


print(to_list(input()))
