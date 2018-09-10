#1.二维有序数组中找目标值是否存在，60&，算法欠优
#第四范式
#s=input().split(" ")
#m=int(s[0])
#n=int(s[1])
#matrix=[]
#for i in range(m):
#    temp=list(map(int,input().split(" ")))
#    matrix.append(temp)
#tar=int(input())
m=3
n=3
matrix=[[2,3,4],[3,4,7],[3,5,8]]
tar=4
ans=[]
for i in range(m):
    if matrix[i][0]<=tar and matrix[i][n-1]>=tar:
        ans=ans+matrix[i]
if tar in ans:
    print("true")
else:
    print("false")
    
    
#头条，leetcode岛屿数，深度优先搜索，深度搜索附近的值并将该位置置0，80%数组越界？
def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    if grid[i][j]:
        grid[i][j] = 0
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)
        dfs(grid, i, j + 1)
#M=int(input())
#grid=[]
#for i in range(M):
#    temp=[]
#    temp=list(map(int,input().split(" ")))
#    grid.append(temp) 
grid=[[1,0,0,1,1],[1,0,0,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
m = len(grid)
if m == 0:
    print(0)
n = len(grid[0])
if n == 0:
    print(0)
res = 0
for i in range(m):
    for j in range(n):
        if grid[i][j]:
            res += 1
            dfs(grid, i, j)
print(res)

#5，找几组人之间互相关注，求有多少个用户是网红（被其他所有人都关注）
#n=int(input())
#m=int(input())
#s=list(map(int,input().split(" ")))
n=3
m=3
s=[1, 2, 2, 1, 2, 3]#表示1关注了2，2关注了1，2关注了3
l_in=[]
users=list(set(s))
i=0
while(i<len(s)):
    temp=[]
    temp.append(s[i])
    temp.append(s[i+1])
    i=i+2
    l_in.append(temp)

def find(item,temp):
    for i in range(len(s)):
        if s[i]==item and i%2==1 and s[i-1] not in temp:
            temp.append(s[i-1])
            temp=find(s[i-1],temp)
    return temp
ans=[]
for item in users:
    temp=[]
    temp.append(item)
    find(item,temp)
    ans.append(temp)
cnt=0
for i in range(len(ans)):
    if len(ans[i])==n:
        cnt=cnt+1
print(cnt)
