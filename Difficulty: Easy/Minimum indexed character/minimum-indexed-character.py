#User function Template for python3

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        #code here
        pat=list(set(pat))
        minidx=float('inf')
        for i in range(len(pat)):
            if pat[i] in Str:
                idx=Str.index(pat[i])
                minidx=min(minidx,idx)
        if minidx==float('inf'):
            return -1
        else:
            return minidx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        print(ans)
# } Driver Code Ends