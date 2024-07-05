#User function Template for python3
class Solution:
	def setBits(self, N):
		# code here
		num=bin(N)[2:]
		c=num.count('1')
		return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends