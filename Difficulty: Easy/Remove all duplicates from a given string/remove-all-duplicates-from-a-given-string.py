#User function Template for python3
class Solution:

	
	def removeDuplicates(self,str):
	    # code here
	    org=[]

	    for i in range(len(str)):
	        if str[i] not in org:
	            org.append(str[i])
	    res=''.join(x for x in org)
	    return res
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends