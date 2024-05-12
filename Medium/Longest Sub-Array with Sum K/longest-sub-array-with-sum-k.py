#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        sumele=0
        l=0
        res=0
        freq={}
        for r in range(n):
            sumele+=arr[r]
            
            if sumele==k:
                res=max(res,r-l+1)
                
            if sumele-k in freq:
                res=max(res,r-freq[sumele-k])
                
            if sumele not in freq:
                freq[sumele]=r
        return res

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends