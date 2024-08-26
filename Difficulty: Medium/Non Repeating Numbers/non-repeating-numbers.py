#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		freq={}
		lst=[]
		
		for num in nums:
		    if num not in freq:
		        freq[num]=1
		    else:
		        freq[num]+=1
		        
		        
	    for k,v in freq.items():
	        if v%2!=0:
	            lst.append(k)
	    return sorted(lst)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends