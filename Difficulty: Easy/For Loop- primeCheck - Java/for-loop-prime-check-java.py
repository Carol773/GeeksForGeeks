import math
class Solution:
    def isPrime(self, n : int) -> str:
        # code here
        if n==1:
            return "No"
        else:
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return "No"
        return "Yes"
        



#{ 
 # Driver Code Starts
import math
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.isPrime(n)
        
        print(res)
        

# } Driver Code Ends