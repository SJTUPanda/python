#s=input().split(";")
s="singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪"
s=s.split(";")
#request=input()
request="请播放周杰伦的七里香给我听"
for i in range(len(s)):
    s[i]=s[i].split("_")
    s[i][1]=s[i][1].split("|")
    
def f(temp):
    if len(temp)==1:
        return temp[0]
    else:
        a=[]
        for i in range(len(temp)):
            a.append(len(temp[i]))
        imax=a.index(max(a))
        return temp[imax]
tar=[]
song=[]    
ans=[]
temp=[]
for i in range(len(s)):
    temp=[]
    ans1=[]
    for j in range(len(s[i][1])):
        if s[i][1][j] in request:
            temp.append(s[i][1][j])
    if temp !=[]:
        ans1.append(s[i][0])
        ans1.append(f(temp))
        if f(temp) not in tar:
            tar.append(f(temp))
        ans.append(ans1)
        
aa=[]
for item in tar:
    a=[]
    for i in range(len(ans)):
        if ans[i][1]==item:
            a.append(ans[i][0])
    aa.append(a)
bb=[]
for i in range(len(aa)):
    aa[i]=sorted(aa[i])
    b=",".join(aa[i])
    bb.append('/'+b)
for i in range(len(tar)):
    request=request.replace(tar[i]," "+tar[i]+bb[i]+" ")
print(request) 
