#User function Template for python3

class Solution:
    def isLucky(self, n): 
        #RETURN True OR False
        if n<=1:
            return True
            
        c=2
        while c<=n:
            if n%c==0:
                return False
            n=n-(n//c)
            c+=1
        return True
        
        
            
            
            
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends