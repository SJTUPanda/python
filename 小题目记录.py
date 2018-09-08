#大写放后面小写放前面，使用‘’替换，实现删除字符
s='asdAAffASASD'
temp=s
ans=""
for i in range(len(s)):
    if s[i].isupper():
        print(s[i])
        ans=ans+s[i]
        temp=temp.replace(s[i],'')
print(temp+ans)
#第二种方法
while(True):
    s=input('')
    if s=="end":
        break
    temp=s
    ans=""   
    for i in range(len(s)):
        if s[i].isupper():
            temp=temp.replace(s[i],"")
            ans=ans+s[i]
    print(temp+ans)

#已知前序和中序，求二叉树的后序排列
def res(pre,tin,ans):
    if pre==[] or tin==[]:
        return ans
    else:
        cur=tin.index(pre[0])
        pre1=pre[1:cur+1]
        pre2=pre[cur+1:]
        tin1=tin[:cur]
        tin2=tin[cur+1:]
    ans=res(pre1,tin1,ans) 
    ans=res(pre2,tin2,ans)
    ans.append(pre[0])   
    return ans
ans=[]
pre=[1,2,4,7,3,5,6,8]
tin=[4,7,2,1,5,3,8,6]
print(res(pre,tin,ans))
