#User function Template for python3
from collections import OrderedDict

class Solution:
    def firstRep(self, s):
        # code here
        freq=OrderedDict()
        
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
                
        for k,v in freq.items():
            if v>1:
                return k
        return '#'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.firstRep(s)
        if ans is '#':
            print(-1)
        else:
            print(ans)
        
# } Driver Code Ends