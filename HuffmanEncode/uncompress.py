import struct


file = 'encoder.txt'#获取huffman编码表
huffman_map = {}
with open(file,'r') as f:
    line = f.readline()
    while line != '':
        lis = line.split(':')
        lis[1] = lis[1].strip()
        huffman_map.update({lis[1]:lis[0]})
        lis.clear()
        line = f.readline()
    f.close()
file = 'compress_data'#获取压缩文件的01序列
f = open(file,'rb')
remain = struct.unpack('B',f.read(1))[0]
datalis = []
data = f.read(1)
while data != b'':
    #先用unpack得到元组，然后[0]选择第一个数 即我们得到的数 然后转换为二进制 形式如0bxxxxxxxx 是字符串，从第二位开始截取字符串
    temp = bin(int.from_bytes(data, byteorder='big', signed=False))[2:]
    temp = '0'*(8-len(temp)) + temp
    datalis.append(temp)
    data = f.read(1)
f.close()
datalis[-1] = datalis[-1].rstrip('0')#由于在编码是补了一些01，现在要把它删除
datalis[-1] = datalis[-1].removesuffix('1')
unzip_data = ''.join(datalis)
file = 'output.txt'
seek = ''
with open(file,'ab') as f:#开始逐个译码
    for i in range(len(unzip_data)):
        seek += unzip_data[i]
        if(huffman_map.get(seek)):
            wri = int(huffman_map[seek])
            f.write(struct.pack('B',wri))
            seek = ''
print('done!')

