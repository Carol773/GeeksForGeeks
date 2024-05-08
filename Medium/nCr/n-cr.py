#User function Template for python3
import math
class Solution:
    def nCr(self, n, r):
        # code here
        if n<r:
            return 0
        if n==r:
            return 1
        nfact=math.factorial(n)
        rfact=math.factorial(r)
        nr=n-r
        nrfact=math.factorial(nr)
        res=((nfact)//(rfact*nrfact))%(1000000007)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends