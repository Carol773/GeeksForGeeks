#User function Template for python3

class Solution:
    def convertToEven(self, s):
        # code here
        s+="E"
        
        return s.count("OE")



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.convertToEven(s)
        print(ans)
# } Driver Code Ends