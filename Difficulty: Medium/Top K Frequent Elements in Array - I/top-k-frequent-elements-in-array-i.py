class Solution:
	def topK(self, nums, k):
		#Code here
		
		freq_count={}
		c=0
		lst=[]
		
		for i in range(len(nums)):
		    if nums[i] not in freq_count:
		        freq_count[nums[i]]=1
		    else:
		        freq_count[nums[i]]+=1
		       
		res=sorted(freq_count.keys(),key=lambda x:(-freq_count[x],-x))
		return res[:k]


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends