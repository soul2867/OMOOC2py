# _*_ coding:gbk _*_

from sys import argv
import os

script, name = argv

filename = open(name,"r+")#打开文件

print filename.read();#打印之前的内容
    
line = raw_input("中文?")#获取输入的内容并保存到line

filename.write(filename.read());#写入之前的

if os.stat(name).st_size != 0:
    filename.write("\n");#判断是否为空
    
filename.write(line);#写入新输入的

filename.close()#保存并关闭文件
