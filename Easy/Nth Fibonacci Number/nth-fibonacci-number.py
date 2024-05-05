
class Solution:
    memo={}
    def nthFibonacci(self, n : int) -> int:
        # code here
        n1=0
        n2=1
        c=0
        
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            while c<n:
                n3=n1+n2
                n1=n2
                n2=n3%1000000007
                c+=1
        return n1


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends