#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        freq={0:-1}
        
        cursum=0
        maxlen=0
        
        for i in range(len(arr)):
            cursum+=arr[i]
            if cursum not in freq:
                freq[cursum]=i
            else:
                maxlen=max(maxlen,i-freq[cursum])
        return maxlen


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends