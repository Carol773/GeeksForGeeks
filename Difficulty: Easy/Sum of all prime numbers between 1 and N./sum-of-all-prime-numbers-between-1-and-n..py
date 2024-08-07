#User function Template for python3
import math

class Solution:
	def prime_Sum(self, n):
		# Code here
		lst=[]
		isPrime=[True]*(n+1)
		i=2
		while i*i<=n:
		    if isPrime[i]:
		        for j in range(i*i,n+1,i):
		            isPrime[j]=False
		    i+=1
		    
		for i in range(2,n+1):
		     if isPrime[i]:
		         lst.append(i)
		return sum(lst)
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends