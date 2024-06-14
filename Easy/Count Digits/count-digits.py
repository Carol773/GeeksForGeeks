#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        N=str(N)
        c=0
        i=0
        
        while i<len(N):
            
            if int(N[i])!=0 and ((int(N)%int(N[i]))==0):
                c+=1
            i+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends