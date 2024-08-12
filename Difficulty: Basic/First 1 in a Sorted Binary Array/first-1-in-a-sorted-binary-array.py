#{ 
 # Driver Code Starts

# } Driver Code Ends
#User function Template for python3

class Solution:
    def firstIndex(self, arr):
    # Your code goes here
        if 1 not in arr:
            return -1
            
        return arr.index(1)



#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.firstIndex(arr))
    
# } Driver Code Ends