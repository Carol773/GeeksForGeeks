#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # code here
        freq={}
        sumele=0
        maxsum=0
        
        for i in range(N):
            if arr[i]==0:
                arr[i]=-1
            sumele+=arr[i]
            
            if sumele==0:
                maxsum=i+1
            
            if sumele in freq:
                maxsum=max(maxsum,i-freq[sumele])
            else:
                freq[sumele]=i
        return maxsum
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends