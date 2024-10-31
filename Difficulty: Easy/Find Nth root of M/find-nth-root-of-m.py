#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		root=m**(1/n)
		root=int(round(root))
		if m==pow(root,n):
		    return root
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