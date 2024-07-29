#User function Template for python3

class Solution:
    def findIndex (self,arr, key ):
        #code here.
        lst=[]
        if key not in arr:
            return [-1,-1]
          
        idx=arr.index(key)  
        lst.append(idx)
        
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==key:
                lst.append(i)
                break
                
       
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    # n=int(input())
    a = list(map(int, input().split()))
    key = int(input())
    ob = Solution()
    ans = ob.findIndex(a, key)
    print(*ans)

# } Driver Code Ends