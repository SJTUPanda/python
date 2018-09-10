round(ans,2)#保留两位小数

import math
log(num,2) #以2为底的对数

import sys
for s in sys.stdin: #输入不确定长度时使用

m ,n = 4,3
matrix = [[0]*n for i in range(m)] #二维列表初始化

l = list(map(lambda x:x**2,number))


b = [1,2,3,4,5]
b.reverse()#反序
b_1 = list(reversed(b))

b.sort()#元素从小到大排序
new_b = sorted(b)#元素从小到大排序

#获得矩阵输入，首先获得数据维数(逗号隔开)，再获得矩阵
str_in=input().split(",")
m=int(str_in[0])
n=int(str_in[1])
l_matrix=[]
for i in range(m):
    str_in_matrix=input().split(",")
    str_in_matrix=list(map(int,str_in_matrix))
    l_matrix.append(str_in_matrix)
    
#获得两个列表中的公共部分      
list_a=[1,2,3,4,5,6]
list_b=[4,5,6,7,8]
a=[item for item in list_a if item in list_b]

#获得列表中不重复元素
l_1=input().split()
l_2=set(l_1)
l_3=[l_1.count(item) for item in l_2]

class TreeNode:#树中节点的定义
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
a=TreeNode(1)

class ListNode:#链表
    def __init__(self, x):
        self.val = x
        self.next = None
