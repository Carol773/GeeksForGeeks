#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        mul=1
        sumele=0
        mod=1000000007
        k=0
        
        for i in range(1,n+1):
            mul=1
            for j in range(1,i+1):
                k+=1
                mul*=k
            sumele+=mul
        return sumele%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends