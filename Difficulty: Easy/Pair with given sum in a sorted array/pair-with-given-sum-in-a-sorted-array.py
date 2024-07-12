#User function Template for python3


class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        c=0
        l=0
        r=len(arr)-1

        while l<r:
            sumele=arr[l]+arr[r]
            if sumele==sum:
                c+=1
            if sumele>sum:
                r-=1
            else:
                l+=1
            
        if c!=0:
            return c
        else:
            return -1
        
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends