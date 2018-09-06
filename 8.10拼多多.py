#1.ac给出血量和攻击方式，休息一轮可以暴击，求最少回合数，贪心
hp=int(input())
no_att=int(input())
buf_att=int(input())
is_no=1
ans=0
def how(no_att,buf_att):
    if no_att>buf_att/2:
        is_no=1
    else:
        is_no=0
    return is_no
if how(no_att,buf_att):
    ans=hp//no_att
    if hp%no_att!=0:
        ans+=1
else:
    ans=2*(hp//buf_att)
    if hp%no_att!=0:
        if hp%no_att<=no_att:
            ans+=1
        else:
            ans+=2
print(ans)

#2 75% 输出两数的商的循环节（无限循环小数的循环体）开始位置和长度
str_in=input().split(" ")
a=int(str_in[0])
b=int(str_in[1])
l_mod=[]
l_ans=[]
ans=0
while(1):
    mod=a%b
    if mod in l_mod:
        print(l_mod.index(mod),len(l_mod)-l_mod.index(mod))
        break
    l_ans.append(a//b)
    l_mod.append(mod)
    if mod==0:
        print(len(l_ans)-1,0)
        break
    else:
        a=mod*10

#之前一场的pdd
#输入一串整数，首先需要将其分成两个部分，每个部分可以加一个小数点也可以不加，
#1.0和010这样的不符合规则，求一共有多少种结果？
def is_all_zero(s):
    for i in s:
        if i!=0:
            return 0
    return 1
def number_of_sub_s(s):
    if is_all_zero(s):
        return 0
    if s[0]==0 and s[-1]==0:
        return 1
    if s[0]==0 or s[-1]==0:
        return 1
    return len(s)
if __name__=='__main__':
    raw_s=input()
    list_s=list(map(int,raw_s))
    if len(list_s)==1:
        print(1)
    ans=0
    for i in range(len(list_s)):
        s1=list_s[:i]
        s2=list_s[i:]
        ans=ans+number_of_sub_s(s1)*number_of_sub_s(s2)
    print(ans)
