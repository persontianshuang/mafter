def me(choose,target):
    end = choose -target
    for index,x in range(0,len(choose)):
        if index<=end:
            f = []
            f.append(x)
            me(choose-1,target-1)
            if len(f)==target:
                pass
        else:
            pass


class Me:
    def __init__(self,choose,target):
        self.c = choose
        self.cc = choose
        self.t = target
        self.tt = target
        self.f = []
        self.r = 1
        self.ff = []

    def me(self,c=-1,t=-1):
        end = self.c -self.t
        # print(end)
        for index,x in enumerate(range(self.r,self.cc+1)):
            if index<=end:
                self.f.append(x)
                # print(self.f)
                if len(self.f)==self.tt:
                    print('succ',self.f)
                    self.f = []
                else:
                    for y in range(x+1,self.cc+1):
                        self.c = self.c -y
                        self.t = self.t -y
                        self.r = self.r +y
                        self.me(self.c,self.t)
                        self.c = self.c +y
                        self.t = self.t +y
                        self.r = self.r -y
            else:
                pass
# Me(4,2).me()

c = 5

all = list(range(c))


# 5*4/2*1=10
f = []
for x in all:
    ff = []
    ff.append(x)
    all = all[1:]
    ff.append(all)
    f.append(ff)
print(f[:-1])
final = f[:-1]
ta = 3
end = c-ta
for index,y in enumerate(end):

    cool = []
    cool.append(y[0])
    cool.append(y[1])
    for z in y[1]:
        cool.append(z)
        if len(cool)==ta:
            cool.pop()
            print()
        else:
            

