import math

def entropyCal(x):
    temp = set(x)#转换成不重复元素的set
    l = len(x)#样本个数
    p= [x.count(i) for i in temp]
    entro = 0.0#信源熵
    for x in p:
        entro += (x/l)*math.log2(l/x)#公式
    return entro

def getData():#获取样本空间
    print("输入样本空间：")
    temp = input()
    item = temp.split(" ")
    return item

if __name__ == '__main__':
    k = getData()
    print("\n信源熵为"+str(entropyCal(k)))