class Stat:
    def __init__(self, d):
        self.d = d
        self.d.sort()
        self.tot = 0
        self.half = len(self.d)/2
        self.keys = []
        self.dic = {}
        self.val = []
        self.big = 0
        self.modes = []
        self.smodes = ""

    def mean(self):
        for i in self.d:
            self.tot += i
        print("The mean is", str(self.tot / len(self.d)) + ".")

    def median(self):
        if len(self.d)%2 == 0:
            print("The median is", str((self.d[int(self.half)] + self.d[int(self.half-1)])/2) + ".")

        else:
            print("The median is", str(self.d[int(self.half - 0.5)]) + ".")

    def mode(self):
        for i in self.d:
            if i not in self.keys:
                self.keys.append(i)
                
        for i in self.keys:
            self.dic[i] = 0

        for i in self.keys:
            for j in self.d:
                if i == j:
                    self.dic[i] += 1
        self.val = self.dic.values()
        
        for i in self.val:
            if i > self.big:
                self.big = i
        
        for i in self.dic:
            if self.dic[i] == self.big:
                self.modes.append(i)
        
        if len(self.modes) == 1 and len(self.modes) != len(self.d):
            print("The mode is", self.modes[0])
        
        elif len(self.modes) > 1 and len(self.modes) != len(self.d):
            print("The modes are", self.modes)

        else:
            print("There is no mode.")


data = []
dat = input("Add your data: ")
while dat !="":
    data.append(int(dat))
    dat = input("Add your data: ")

if data != []:
    stat = Stat(data)
    print(stat.d)
    stat.mean()
    stat.median()
    stat.mode()