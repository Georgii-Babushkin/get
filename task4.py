def _abs(a):
    return(-abs(a))

def sort_list(lst):
    lst.sort(key=_abs)
    print(lst)
    return int(lst[0]) + int(lst[-2])


list = []
list += map(int, input().split())
print(sort_list(list))
