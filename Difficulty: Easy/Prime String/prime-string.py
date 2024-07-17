#User function Template for python3
from math import sqrt
class Solution:
    def isPrimeString(self, s):
        # code here
        sum_words=0
        
        for ch in s:
            sum_words+=ord(ch)
        if sum_words>1:
            for i in range(2,sum_words):
                if sum_words%i==0:
                    return False
                    
            return True
        return False
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        ob = Solution()
        ans = ob.isPrimeString(s)
        if ans:
            print("YES")
        else:
            print("NO")
        
# } Driver Code Ends