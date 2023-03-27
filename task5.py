class tasker:
    def __init__(self, _str = input()):
        self.lst1 = _str.split()
        self.lst2 = _str.split()
    def method1(self):
        print(len(self.lst1))

    def method2(self):
        self.lst2 = self.lst2[0:-1]
        sum = 0
        for i in range(len(self.lst1) - 1):
            self.lst2[i] = str(float(self.lst1[i]) + float(self.lst1[i + 1]))
            sum += float(self.lst1[i]) + float(self.lst1[i + 1])
        if int(sum) == sum:
            sum = int(sum)
        print(sum)

    def method3(self):
        lstN = []
        sum = 0
        for i in range(1, len(self.lst1)):
            lstN += str(i)
        lstN = self.lst1 + lstN
        for i in range(0, len(lstN), 3):
            sum += float(lstN[i])
        if int(sum) == sum:
            sum = int(sum)
        print(sum)


a = tasker()
a.method1()
a.method2()
a.method3()