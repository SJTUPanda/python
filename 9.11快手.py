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
###############################33
#s=list(map(int,input().split(" ")))
#N=s[0]
#M=s[1]
#mat=list(map(int,input().split(" ")))
N=7
M=2
matrix=[4, -3, 4, -2, 3, -1, 100,2,2,2,-9,3,9]
#N=7
#M=4
#mat=[1,2,3,-2,3,-10,3]
m=[]
m.append(matrix[0])
temp=0
#正负相间隔
for i in range(1,len(matrix)):
    if m[-1]*matrix[i]>0:
        m[-1]+=matrix[i]
    else:
        m.append(matrix[i])
    print("m:",m)
if m[0]<0:
    m.pop(0)
if m[-1]<0:
    m.pop(-1)
#统计正数数目
p_num=0
p_list=[]
for num in m:
    if num>0:
        p_num+=1
        p_list.append(num)
print("p_num0:",p_num)   
def biggest_i(m):
    bigger=float("inf")
    bigger=-1*bigger
    for num in m:
        if num>bigger and num<0:
            bigger=num
    return m.index(bigger)
def f(m,p_num,M):        
    if p_num<=M:
        a=0
        for item in m:
            if item>0:
                a+=item
        print(m)
        print(a)
    else:
        tar_i=biggest_i(m)
        if tar_i+2>=len(m):
            m[tar_i-1]=m[tar_i-1]+m[tar_i]+m[tar_i+1]
            m=m[:tar_i]
        else:
            m[tar_i-1]=m[tar_i-1]+m[tar_i]+m[tar_i+1]
            m=m[:tar_i]+m[tar_i+2:]        
        print("new m:",m)       
        p_num=p_num-1
        print("p_num",p_num)
        f(m,p_num,M)
f(m,p_num,M)       

#######别人的代码，快手第三题
## N, M = list(map(int, input().split()))
## ns = list(map(int, input().split()))
#N, M = 7, 3
#ns = [4, -3, 4, -2, 3, -1, 100]
#
#new_ns = []
#tmp = ns[0]
#cnt_pos = 0  # 正数块的数量
#for i in ns[1:] + [0]:  # trick
#    if i != 0 and (tmp > 0) == (i > 0):  # 跳过 0
#        tmp += i
#    else:
#        if tmp > 0:
#            cnt_pos += 1
#        new_ns.append(tmp)
#        tmp = i
#
## new_ns.append(tmp)
#
#print(new_ns)  # [6, -2, 3, -10, 3]
#print(cnt_pos)  # 3
#
## 去掉首尾的负数块
#if len(new_ns) >= 1 and new_ns[0] < 0:
#    new_ns.pop(0)
#
#if len(new_ns) >= 1 and new_ns[-1] < 0:
#    new_ns.pop(-1)
#
#print(new_ns)  # [6, -2, 3, -10, 3]
#
## 按奇偶划分奇数和偶数块
#ns_pos = new_ns[0::2]
#ns_neg = new_ns[1::2]
#print(ns_pos)  # [6, 3, 3]
#print(ns_neg)  # [-2, -10]
#
## 如果 M 的值小于正数块的数量则进行合并
#updated = True
#while updated and M < cnt_pos:
#    """"""
#    updated = False
#
#    mx_i = 0
#    # mx = max(ns_pos[mx_i] + ns_pos[mx_i+1] + ns_neg[mx_i], ns_pos[mx_i], ns_pos[mx_i])
#    mx = float("-inf")
#    for i in range(len(ns_neg)):
#        tmp = ns_pos[i] + ns_pos[i+1] + ns_neg[i]
#        if tmp < max(ns_pos[i], ns_pos[i+1]):  # 如果合并后减小则不合并
#            continue
#        if tmp > mx:
#            updated = True
#            mx = tmp
#            mx_i = i
#    if updated:
#        # 更新合并后的数组
#        ns_neg.pop(mx_i)
#        ns_pos[mx_i] = mx
#        ns_pos.pop(mx_i+1)
#        cnt_pos -= 1
#    # print(ns_pos)
#    # print(ns_neg)
#ns_pos.sort(reverse=True)
#print(sum(ns_pos[:M])) 
