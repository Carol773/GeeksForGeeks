#User function Template for python3
class Solution:
	def countSubstr(self, S):
		# your code here
		count=S.count("1")
		if count==1 or count==0:
		    return 0
		else:
		    return count*(count-1)//2
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.countSubstr (s))

	# Contributed By: Pranay Bansal
# } Driver Code Ends