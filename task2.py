def read(a):
    lst = ''
    i = 1
    while a[i] != ']':
        lst += a[i]
        i += 1
    if lst != '':
        return lst.split(', ')
    else:
        return []


def change_sum_lst(lst):
    sum = 0
    lst[0], lst[-1] = lst[-1], lst[0]
    i = 0
    while i < len(lst):
        lst[i] = 0
        i += 2
    for i in lst:
        sum += float(i)
    return sum


a = read(input())
sum = change_sum_lst(a)
if int(sum) == sum:
    print(int(sum))
else:
    print(sum)
