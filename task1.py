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


a = read(input())
sum2 = 0
summ = 0
if len(a) > 0:
    for i in a:
        i = float(i)
        if (int(i) == i) and (int(i) % 2 == 0):
            sum2 += int(i)
        summ += i
    if int(summ) == summ:
        summ = int(summ)
    print(len(a))
    print(summ)
    print(sum2)
    print(a[len(a) // 2 - (len(a) - 1) % 2])
else:
    print('Список пустой')
