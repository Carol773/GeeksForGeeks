#User function Template for python3
class Solution:
	def isPanagram(self, S):
		# code here
		lst=set()
		for i in range(len(S)):
		    lst.add(S[i].lower())
		if len(lst)>=26:
		    return 1
		else:
		    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends