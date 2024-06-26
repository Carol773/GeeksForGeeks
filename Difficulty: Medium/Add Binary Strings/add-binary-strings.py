#User function Template for python3
class Solution:
	def addBinary(self, A, B):
		# code here
		A=int(A,2)
		B=int(B,2)
		
		res=A+B
		ans=bin(res)
		ans=ans[2:]
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends