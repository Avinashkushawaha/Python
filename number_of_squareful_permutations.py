import math
from functools import lru_cache

def numSquarefulPerms(A):
    n=len(A)
    A.sort()
    adj=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if int(math.isqrt(A[i]+A[j]))**2==A[i]+A[j]:
                adj[i][j]=True
    
    @lru_cache(None)
    def dfs(i,mask):
        if mask==(1<<n)-1:
            return 1
        ans=0
        for j in range(n):
            if not mask>>j&1 and adj[i][j]:
                if j>0 and A[j]==A[j-1] and not mask>>(j-1)&1: continue
                ans+=dfs(j,mask|(1<<j))
        return ans
    
    ans=0
    for i in range(n):
        if i>0 and A[i]==A[i-1]: continue
        ans+=dfs(i,1<<i)
    return ans
