#User function Template for python3

class Solution:
    def closing (self,s, pos):
        # your code here
        c=0
        
        for i in range(pos,len(s)):
            if s[i]=='[':
                c+=1
            if s[i]==']':
                c-=1
                if c==0:
                    return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    pos = int (input ())
    ob = Solution()
    print (ob.closing (s, pos))
    
# Contributed By: Pranay Bansal

# } Driver Code Ends