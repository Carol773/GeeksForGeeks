#User function Template for python3

class Solution:
    def isKSortedArray(self, arr, n, k): 
        #code here.
        dc={num:ind for ind,num in enumerate(arr)}
        arr.sort()
        
        for i in range(n):
            if abs(i-dc[arr[i]])>k:
                return "No"
        return "Yes"



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    ob = Solution()
    print(ob.isKSortedArray(a, n, k))

# } Driver Code Ends