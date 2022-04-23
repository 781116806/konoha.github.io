import huffman
import struct
file = '鲁迅全集.TXT'
count = {}
with open(file,'rb') as f:#逐个读入字节，然后对字节操作
    onebyte = f.read(1)
    while onebyte != b'':#终止条件
        dec = str(int.from_bytes(onebyte, byteorder='big', signed=False))#将16进制转成10进制数，再转为字符
        if count.get(dec):#构造dict
            count[dec] += 1
        else:
            count[dec] = 1
        onebyte = f.read(1)
    f.close()
tree = huffman.huffmanTree(count)#构造huffman编码
tree.previsit(tree.root,'')#获得编码的文件，文件名是encoder.txt
huffman_map = {}#huffman词典，用于编码翻译
file = 'encoder.txt'#读取我们获得的huffman编码
with open(file,'r') as f:
    temp = f.readline()
    while temp != '':
        lis = temp.split(':')
        lis[1] = lis[1].strip()
        huffman_map.update({lis[0]:lis[1]})
        temp = f.readline()
file = '鲁迅全集.TXT'#需要编码的txt
newfile = 'compress_data'#写入的文件
write_data = ''
with open(file,'rb') as f1:
    onebyte = f1.read(1)
    while onebyte != b'':
        dec = str(int.from_bytes(onebyte, byteorder='big', signed=False))#将16进制转换为十进制
        write = huffman_map[dec]#转码
        write_data += write#储存起来
        onebyte = f1.read(1)
    f1.close()
    remain = len(write_data)%8#计算末尾还剩余几位，如果不足八位，则需要补位
with open(newfile,'ab') as f2:
    f2.write(struct.pack('B', len(write_data) % 8))
    for index in range(0,len(write_data),8):#未到末尾，则直接写入
        if index + 8 < len(write_data):
            f2.write(struct.pack('B',int(write_data[index:index+8],2)))
        else:#到达末尾
            if remain == 0:#判断剩余几位
                f2.write(struct.pack('B',int(write_data[index:],2)))
            else:#不足八位就补100....  就是先补一个1，再后续补0  直到八位为止
                temp = write_data[index:] + '1' + '0'*(8-remain-1)
                f2.write(struct.pack('B',int(temp,2)))
    f2.close()
print('done!')