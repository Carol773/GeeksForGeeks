#User function Template for python3

class Solution:

    def countStr(self, n):
        # code here
        return 1+(n*2)+(n*((n*n)-1)//2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends