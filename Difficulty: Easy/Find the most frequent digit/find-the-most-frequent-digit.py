#User function Template for python3

class Solution:

    def solve(self, N):
        # code here
        f=-1
        m=-1
        
        for i in N:
            if N.count(i)>f:
                m=i
                f=N.count(i)
            elif N.count(i)==f:
                if int(i)>int(m):
                    m=i
            else:
                pass
        return m
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = input()

        solObj = Solution()

        print(solObj.solve(N))
# } Driver Code Ends