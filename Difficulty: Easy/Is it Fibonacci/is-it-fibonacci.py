#User function Template for python3
import math
class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        n=len(GeekNum)
        for i in range(n,N):
            next_geek=sum(GeekNum[abs(i-K):i])
            GeekNum.append(next_geek)
        return GeekNum[-1]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
    
# } Driver Code Ends