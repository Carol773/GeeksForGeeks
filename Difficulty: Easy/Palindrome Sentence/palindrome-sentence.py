#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
		# your code here
		lst=[]
		
		for ch in s:
		    if ch.isalpha():
		        lst.append(ch)
		
		s=''.join(x for x in lst)
		if s==s[::-1]:
		    return 1
		else:
		    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		if ob.sentencePalindrome (s):
			print (1)
		else:
			print (0)
# } Driver Code Ends