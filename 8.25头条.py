#判断每一组中的字符串是否有双生词，组成环后正序或者逆序能够得到对方，未通过，测试可以通过
t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    l=[]
    flg=0
    for j in range(n):
        l_raw=list(input())
        l.append(l_raw)
    B=l[0]+l[0]
    C=l[0][::-1]+l[0][::-1]
    for j in range(n):
        A=l[j]
        if j!=0 and (any([A==B[i:i+len(A)] for i in range(0,len(B)-len(A)+1)]) or any([A==C[i:i+len(A)] for i in range(0,len(C)-len(A)+1)])):
            flg=1
            break
        else:
            flg=0
    if flg==0:
        ans.append('Sad')
    else:
        ans.append('Yeah')
for item in ans:
    print(item)
    
#上面双生词中包含了最长递增子序列问题，待解决
