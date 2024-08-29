#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        #code here
        c=0
        idx=0
        min_one=float('inf')
        for i in range(n):
            for j in range(m):
                if a[i][j]==1:
                    c+=1
            if c<min_one:
                min_one=c
                idx=i+1
            c=0
        return idx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends