#User function Template for python3
from collections import Counter
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		ans=''
		q=[]
		count=Counter()
		
		for ch in A:
		    count[ch]+=1
		    q.append(ch)
		    
		    while q and count[q[0]]>1:
		        q.pop(0)
		        
		    if q:
		        ans+=q[0]
		    else:
		        ans+='#'
		return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends