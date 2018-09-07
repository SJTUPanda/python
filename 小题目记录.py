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
