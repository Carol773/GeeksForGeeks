#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        ans=''
        
        while n:
            n-=1
            r=n%26
            ans=chr(ord('A')+r)+ans
            n=n//26
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends