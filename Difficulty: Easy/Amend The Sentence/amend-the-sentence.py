#User function Template for python3
import re

class Solution:

    def amendSentence(self, s):
        res=''
        
        for i in range(len(s)):
             if s[i].isupper():
                 res+=' '+s[i].lower()
             else:
                 res+=s[i]
        return res.lstrip()
             
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.amendSentence(s))
        

# } Driver Code Ends