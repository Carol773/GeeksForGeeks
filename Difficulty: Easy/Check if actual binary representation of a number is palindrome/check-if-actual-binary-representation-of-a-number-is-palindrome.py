#User function Template for python3
class Solution:
	def binaryPalin (self, N):
		# Your Code Here
		bin_rep=bin(N)
		bin_new=bin_rep[2:]
		if bin_new==bin_new[::-1]:
		    return 1
		else:
		    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		ob = Solution()
		print(ob.binaryPalin(n))

	# Contributed By: Pranay Bansal

# } Driver Code Ends