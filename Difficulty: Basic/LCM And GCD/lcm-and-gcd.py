#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here
        def gcd(A,B):
            while B!=0:
                rem=A%B
                A=B
                B=rem
            return A
        lcm=(A*B)//gcd(A,B)
        while B!=0:
                rem=A%B
                A=B
                B=rem
        ans=A
        return lcm,ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends