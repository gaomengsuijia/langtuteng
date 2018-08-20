from django.test import TestCase

# Create your tests here.

#冒泡排序

def maopao(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] >lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    print(lis)

maopao([3,4,5,1,7,89,40])

#用一个尺子做中介来计算

def chizi(lis):
    flag = lis[0]
    for i in range(len(lis)):
        if lis[i] > flag:
            flag = lis[i]
    print(flag)

chizi([3,4,5,1,7,89,40])

#列表组合，然后排序

import random
a = [random.randrange(1,100) for i in range(10)]
b = [random.randrange(1,100) for j in range(5)]
def get_zuixiao(lis,is_choose):
    set_min = False
    k = -1
    min = None
    for i in range(len(lis)):
        if is_choose.get(i,0) == 1:
            continue#已经选出，不用处理了

        if not set_min:
            min = lis[i]
            set_min = True
            k = i

        else:
            if lis[i] < min:
                min = lis[i]
                k = i

    return k



# print(a,'--',get_zuixiao(a,is_choose={}))
# print(b,'--',get_zuixiao(b,is_choose={}))
print("a == ",a)
print("b== ",b)
a_is_choose = {}
b_is_choose = {}
c = []
while True:
    m = get_zuixiao(a,a_is_choose)
    n = get_zuixiao(b,b_is_choose)
    if m==-1 and n==-1:
        #全部取出，结束
        break
    if m == -1:
        #a数组已经取完了
        c.append(b[n])
        b_is_choose[n] = 1
    elif n == -1:
        #b数组已经取完了
        c.append(a[m])
        a_is_choose[m] = 1
    else:
        if a[m] > b[n]:
            c.append(b[n])
            b_is_choose[n] = 1
        else:
            c.append(a[m])
            a_is_choose[m] = 1

print(c)


