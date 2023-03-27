class sixth:
    def __init__(self, cnt, first, step):
        self.cnt = int(cnt)
        self.first = float(first)
        self.step = float(step)
        self.lst = ['' for i in range(cnt)]
        for i in range(cnt):
            self.lst[i] = str(first + step * i)

    def konk(self):
        if int(self.first) == self.first:
            self.first = int(self.first)
        ret = str(self.first)
        if self.cnt >=2:
            for i in range(2, self.cnt, 2):
                ret += '-' + str(self.lst[i])
        return ret

    def info(self):
        print(self.cnt)
        if self.step >= 0:
            Max = self.lst[self.cnt - 1]
            Min = self.lst[0]
        else:
            Min = self.lst[self.cnt - 1]
            Max = self.lst[0]
        print('Min -', Min)
        print('Max -', Max)
        print('sum -', float(Min) + float(Max))

    def New(self):


a = sixth(10, 2, 1)
print(a.lst)
print(a.konk())
a.info()