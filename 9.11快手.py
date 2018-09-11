#########1统计字母输入次数
#s="babcc"
s=list(input())
temp=[]
ans=""
set_s=list(set(s))
set_s.sort()#可以将字母按照顺序排列
for char in set_s:
    temp.append(s.count(char))
for i in range(len(set_s)):
    ans+=set_s[i]+str(temp[i])
print(ans)


###########2，以2的次幂方式进行跳楼梯
a=[1,1]
i=2
while(i<=1000):
    x=0
    temp=0
    while((i-2**x)>=0):
        temp=temp+a[i-2**x]
        x=x+1
    a.append(temp)
    i=i+1
m=int(input())
in_list=[]
for i in range(m):
    num=(int(input()))
    print((a[num])%(10**9+3))
    
    
###################3
#    作者：n不正
#链接：https://www.nowcoder.com/discuss/106768
#来源：牛客网
#
#1、先把整个数组改成正负交错的数组，去掉首尾的负数(相邻的正数合并成一个正数，负数合并成一个负数) 
#2、如果正数个数<=M，输出所有的正数之和
#3、如果正数个数>M，将数组中[正负正]合并，该负数为数组中负数的最大值并且三者之和>三者最大值
#4、直到3不满足或者正数个数<=M,输出最大的M个正数之和
