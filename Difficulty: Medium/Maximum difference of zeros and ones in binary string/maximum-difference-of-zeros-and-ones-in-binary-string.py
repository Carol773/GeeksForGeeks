#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		curDiff=0
		maxDiff=-1
		
		for ch in S:
		    value=-1
		    if ch=='0':
		        value=1
		    curDiff+=value
		    maxDiff=max(maxDiff,curDiff)
		    if curDiff<0:
		        curDiff=0
		return maxDiff
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends