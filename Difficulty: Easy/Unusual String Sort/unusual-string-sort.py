#User function Template for python3

class Solution:
    def stringSort (self,s):
        # your code here
        upper=[]
        lower=[]
        
        res=''
        
        s=sorted(s)
        for ch in s:
            if ch.isupper():
                upper.append(ch)
            else:
                lower.append(ch)
        i=0
    
        l=min(len(upper),len(lower))
        while i<l:
            res+=upper[i]+lower[i]
            i+=1
                

        while i<len(upper):
            res+=upper[i]
            i+=1
            
        while i<len(lower):
            res+=lower[i]
            i+=1
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.stringSort (s))
    
#  Contributes By: Pranay Bansal
# } Driver Code Ends