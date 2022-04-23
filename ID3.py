import math
import copy

'''
前言：
chara： 就是特征 character
'''

def DataInit():#数据集初始化
    dataSet = [
        ['sunny','hot','high','weak','no'],
        ['sunny','hot','high','strong','no'],
        ['overcast','hot','high','weak','yes'],
        ['rain','mild','high','weak','yes'],
        ['rain','cool','normal','weak','yes'],
        ['rain','cool','normal','strong','no'],
        ['overcast','cool','normal','strong','yes'],
        ['sunny','mild','high','weak','no'],
        ['sunny','cool','normal','weak','yes'],
        ['rain','mild','normal','weak','yes'],
        ['sunny','mild','normal','strong','yes'],
        ['overcast','mild','high','strong','yes'],
        ['overcast','hot','normal','weak','yes'],
        ['rain','mild','high','strong','no']
        ]
    labels = ['outlook','temperature','humidity','wind']
    return dataSet,labels
'''
信源熵计算
输入的是一个countlist,计算总和,然后计算概率,代入公式得到信源熵
'''
def entropyCal(countlist):#信源熵计算
    s = sum(countlist)
    entro = 0.0
    for i in countlist:
        if(i == 0):#i为0则不计算
            pass
        else:
            entro += (i/s)*math.log2(s/i)#公式
    return entro

'''
增益值计算 输入特征 数据集 和标签集合 然后得到对应的增益值
'''
def gainCal(chara,dataset,labels):#计算对应特征的增益值
    index = labels.index(chara)#返回特征对应的索引
    charalist = list(set([item[index] for item in dataset]))#返回没有重复值的特征具体分类
    count = []
    for item in charalist:
        num = 0
        sum = 0
        for k in dataset:
            if k[index] == item:
                sum = sum + 1
                if  k[-1] == dataset[0][-1]:#一般来说决策只有两种，yes或者no，所以这里是数其中一种决策，用总数减去另一种得到二分布
                   num = num + 1
        temp = [num, sum - num]
        count.append(temp)
    sumEntro = 0.0
    for item in count:
        sumEntro += entropyCal(item)
    return sumEntro

'''
获得增益值最大的标签，输入数据集和标签集，分别计算增益值，然后得到最佳标签
'''

def getBestChara(dataset,labels):#对label中的标签进行迭代，得到各自的增益值，然后从中选择一个增益值最大的标签
    print('剩余标签：')
    print(labels)
    gain = [gainCal(chara,dataset,labels) for chara in labels]
    return labels[gain.index(max(gain))]

'''
返回决策里的多数成员
'''

def majorOf(classlist):#返回列表里的major成员，也就是主要成员
    classtype = list(set(classlist))#先转set再转回list
    count = [classlist.count(item) for item in classtype]#创建一个数量的列表，和上面list成员一一对应
    return classtype[count.index(max(count))]#返回最大值

'''
用来分割数据集，分割的时候不会改变原数据集，返回一个新的数据集
'''

def spiltDataset(dataset,index):
    typelist = list(set([item[index] for item in dataset]))
    asdataset = []
    for type in typelist:
        temp = []
        for item in dataset:
            if item[index] == type:
                temp.append(item)
        print(temp)
        for new in temp:
            new.pop(index)
        asdataset.append(temp)
    print('\n')
    return asdataset,typelist

'''
检验结果的时候发现的问题，list作为参数传进函数里面，不会作为临时参数，导致递归的时候数据丢失，所以验算的时候发现决策树有问题
解决方案：新写一个remove函数，用copy包实现返回一个全新的list，不会干扰原来的list
'''

def MyRemove(source,index):#不改变原list，返回一个新的list
    temp = copy.deepcopy(source)
    temp.pop(index)
    return temp

'''
核心函数，递归完成决策树的绘制
'''

def createTree(dataset,labels):
    classlist = [item[-1] for item in dataset]#获取所有决策的集合，方便判断
    #两个递归出口
    if classlist.count(classlist[0]) == len(classlist):#如果筛选后的样本里只有一种决策，就返回这种选择
        return classlist[0]
    if len(labels) == 0:#如果没有标签可以供我们进行划分了 就返回决策中的最多数
        return majorOf(classlist)
    bestchara = getBestChara(dataset,labels)#定义一个增益最大的标签
    print(bestchara)#这一列是用来检查递归是否正确
    index = labels.index(bestchara)#获取bestchara索引值
    afDataset, typelist = spiltDataset(dataset,index)#分割由最佳标签为基准得到的数据集,af即after spilt
    nlabels = MyRemove(labels,index)#将最佳标签去除，方便下一步分割
    temp = {}
    for i in range(len(typelist)):#递归调用createTree
        temp.update({typelist[i]:createTree(afDataset[i],nlabels)})
    Tree = {bestchara:temp}
    return Tree

def main():
    Dataset, Labels = DataInit()
    Tree = createTree(Dataset,Labels)
    print(Tree)

if __name__ == '__main__':
    main()