#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	lst=[]
    	fact=1
    	
    	for i in range(1,n+1):
    	    fact*=i
    	    if fact<=n:
    	        lst.append(fact)
    	    else:
    	        break
    	return lst
    	
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends