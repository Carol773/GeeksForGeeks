#User function Template for python3

class Solution:
    def safePos(self, n, k):
        # code here 
        arr=[]
        
        for i in range(1,n+1):
            arr.append(i)
         
        i=0   
        while n>1:
            r=(i+k-1)%n
            del arr[r]
            n-=1
            if r==n:
                i=0
            i=r
        return arr[0]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,k=map(int,input().split())
        
        ob = Solution()
        print(ob.safePos(n,k))
# } Driver Code Ends