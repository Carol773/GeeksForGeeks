#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		# Code here
		n=str(n)
		res=n[::-1]
		return int(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends