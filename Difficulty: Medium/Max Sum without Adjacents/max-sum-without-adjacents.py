#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		max_val=0
		if len(arr)==0:
		    return 0
		elif len(arr)==1:
		    return arr[0]
		elif len(arr)==2:
		    return max(arr[0],arr[1])
		else:
		    val1=arr[0]
		    val2=max(arr[0],arr[1])
		    
		    for i in range(2,len(arr)):
		        max_val=max(val1+arr[i],val2)
		        val1=val2
		        val2=max_val
		    return max_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends