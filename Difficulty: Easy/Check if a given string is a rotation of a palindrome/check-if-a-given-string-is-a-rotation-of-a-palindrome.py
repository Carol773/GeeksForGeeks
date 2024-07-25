#User function Template for python3
class Solution:
	def isRotatedPalindrome(self, s):
		#code here
		ln = len(s)
		
		def is_pal(sub):
		    
		    l = 0
		    
		    r = ln-1
		    
		    
		    while l <=r:
		        
		        if sub[l] != sub[r]:
		            
		            return False
		            
		            
		            
		        l+=1
		        
		        r-=1
		        
		        
		    return True
		
		
		
		for i in range(ln):
		    
		    sub = s[i:] + s[:i]
		    
		    if is_pal(sub):
		        
		        return 1
		        
		        
		return 0
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.isRotatedPalindrome(s)
		print(answer)
		
# } Driver Code Ends