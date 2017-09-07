import itertools


x0 = [1,2]
x1 = [1,2,3]
x2 = [2,3]
x3 = [1,3]
x4 = [1,3]

all = [x0,x1,x2,x3,x4]

def me(choose,target):
    l2 = list(itertools.permutations(range(choose),target))
    l3 = [x for x in l2 if list(x)==sorted(list(x))]
    return l3

# print(me(4,2))
# print(me(len(all),5))
haa = set()
for x in me(len(all),5):
    fi = [all[xx] for xx in x]
    print(fi)
    exec ('[haa.add(i) for i in itertools.product({})]'.format(str(fi)[1:-1]))

print(len(haa))

# add set

# for x in x1:
#     for a in x2:
#         for b in x3:
# print(x,a,b)


# print list(itertools.combinations(['a','b','c'],2))
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
# combinations（）函数返回的是这样的列表。无重复的。
