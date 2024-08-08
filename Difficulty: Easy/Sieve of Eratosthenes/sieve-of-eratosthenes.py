#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	lst=[]
    	
    	isPrime=[True]*(N+1)
    	
    	i=2
    	
    	while i*i<=N:
    	    if isPrime[i]:
    	        for j in range(i*i,N+1,i):
    	            isPrime[j]=False
    	    i+=1
    	    
    	for i in range(2,N+1):
    	    if isPrime[i]:
    	        lst.append(i)
    	return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends