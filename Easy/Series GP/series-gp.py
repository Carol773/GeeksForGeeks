#User function Template for python3
import math
class Solution:
	def Nth_term(self, a, r, n):
		# Code here
		mod=1000000007
		power=pow(r,n-1,mod)
		res=(a*power)%mod
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a, r, n = input().split()
		a = int(a)
		r = int(r)
		n = int(n)
		ob = Solution()
		ans = ob.Nth_term(a, r, n)
		print(ans)
# } Driver Code Ends