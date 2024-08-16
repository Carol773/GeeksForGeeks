
#User function Template for python3

class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        #code here
        
        lst=[]
        
        for i in range(len(s1)):
            if s1[i] not in s2:
                lst.append(s[i])
                
        for i in range(len(s2)):
            if s2[i] not in s1:
                lst.append(s2[i])
        
        res=''.join(x for x in lst)
        if res:
            return res
        else:
            return -1
            
        


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
        print(obj.concatenatedString(s,p))
# } Driver Code Ends