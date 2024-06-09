#User function Template for python3
import math

class Solution:
	def NthRoot(self, n, m):
		# Code here
		digit=pow(m,1/n)
		digit=int(round(digit))
		
		if pow(digit,n)==m:
		    return digit
		else:
		    return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends