#User function Template for python3

class Solution:
    def pattern(self, N):
        # code here
        org=N
        ans=[N]
        
        while N>0:
            N=N-5
            ans.append(N)
        while N!=org:
            N=N+5
            ans.append(N)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends