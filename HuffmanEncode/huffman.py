class Node(object):
    def __init__(self,name = None,value = None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self,other):
        return self.value < other.value


class huffmanTree(object):
    def __init__(self,weights):##weights即权值的dict 一个符号对应一个权
        self.root = None
        self.nodes = [Node(n[0],n[1]) for n in weights.items()]
        self.l = len(self.nodes)
        for i in range(1,self.l):
            self.nodes.sort()##排序重新得到最小的两个
            temp = Node(value=self.nodes[0].value+self.nodes[1].value)
            temp.left = self.nodes.pop(0)
            temp.right = self.nodes.pop(0)
            self.nodes.append(temp)
            if i == self.l-1:
                self.root = temp
  
    def previsit(self,node,encode):
        if node.name != None:
            f = open("encoder.txt", "a")    # 打开文件以便写入
            print(f'{node.name}:{encode}',file=f)
            f.close  #  关闭文件

            return
        else:
            self.previsit(node.left,encode+'0')
            self.previsit(node.right,encode+'1')

            


