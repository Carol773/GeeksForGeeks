class Solution:
    def thirdLargest(self,arr):
        # code here
        arr=sorted(arr,reverse=True)
        
        if len(arr)<3:
            return -1
        else:
            return arr[2]


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))

# } Driver Code Ends