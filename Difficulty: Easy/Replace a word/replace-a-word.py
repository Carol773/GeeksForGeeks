#User function Template for python3
class Solution:
    def replaceAll (ob, S, oldW, newW):
        # code here 
        
        #S.split(oldW)
        
        news=S.replace(oldW,newW)
        return news

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        oldW = input()
        newW = input()
        
        ob = Solution()
        print(ob.replaceAll(S, oldW, newW))
# } Driver Code Ends