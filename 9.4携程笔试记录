#输入相同空间的p和q，求计算kullback-leibler距离（KL距离），sum[P1(x).log(P1(x)/P2(x))]
#表示两组离散数据的信息量，相对熵，66%通过，不知道原因

import math
p=input().split(" ")
p=list(map(int,p))
q=input().split(" ")
q=list(map(int,q))
#p=[1 ,1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 3, 4, 1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 1, 3, 1]
#q=[2, 2, 2 ,2 ,3 ,4 ,4 ,2, 2, 1, 2, 4, 3, 2, 2, 1, 3, 4, 4, 2, 4, 3]
p_set=list(set(p))
q_set=list(set(q))
sum=0
for num in p_set:
px=p.count(num)/len(p)
qx=q.count(num)/len(q)
sum=sum+px*math.log(px/qx,2)
print(round(sum,2))
