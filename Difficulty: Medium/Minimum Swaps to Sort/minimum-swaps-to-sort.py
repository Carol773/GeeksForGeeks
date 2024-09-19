

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		s=sorted(nums)
		c=0
		freq={}
		
		if s==nums:
		    return 0
		    
		for i in range(len(nums)):
		    freq[nums[i]]=i
		    
		for i in range(len(nums)):
		    if nums[i]!=s[i]:
		        n=freq[s[i]]
		        nums[i],nums[n]=nums[n],nums[i]
		        c+=1
		        freq[nums[n]]=n
		        freq[nums[i]]=i
		return c
		    

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends