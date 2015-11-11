# W1：极简交互式笔记系统

* 
 之前加班拖延太重，这周开始争取跟上大部队。
*  
第一周任务根据芝麻星中的卡片提示，参考笨办法13题~17题




## **本周整体任务概述:**



* 
完成一个极简交互式笔记系统,需求如下:

  * 
一次接收输入一行笔记

  * 
保存为本地文件

  * 
再次运行系统时,能打印出过往的所有笔记

* 
发布: 发布到各自仓库的 _src/om2py0w/0wex1/ 目录中
* 
指标:
包含软件使用说明书: README.md，能令其它学员根据说明书,运行系统,完成所有功能

**环境**

* 系统：Win10




**开发过程
**
* 
调用脚本 main.py，待在PowerShell中运行之

* 
建立同名txt文档：main.txt，存放于同一文件夹

* 
解包(unpack)参数script，name=argv #script=main.py, name=main.txt

```from sys import argv
import os

script, name = argv```






