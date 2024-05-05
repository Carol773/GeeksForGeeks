#User function Template for python3
import re
class Solution:
    def reverseEqn(self, s):
        tokens=re.split(r'([-+*/])',s)
        res=tokens[::-1]
        ans=''.join(x for x in res)
        return ans
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends