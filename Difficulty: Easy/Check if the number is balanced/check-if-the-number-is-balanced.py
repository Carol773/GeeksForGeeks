#User function Template for python3
class Solution:
	def balancedNumber(self, N):
		# your code here
		
		N=str(N)
		l=len(N)-1
		mid=(l+1)//2
		sum_l=0
		sum_r=0
	
		for i in range(mid):
		    sum_l+=int(N[i])
		    
		for i in range(mid+1,len(N)):
		    sum_r+=int(N[i])
		
		if sum_l==sum_r:
		    return 1
		else:
		    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		N = input ()
		ob = Solution()
		if ob.balancedNumber(N):
			print (1)
		else:
			print (0) 
# } Driver Code Ends