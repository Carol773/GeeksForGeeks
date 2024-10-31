#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        # code here
        min_num=min(arr)
        return arr.index(min_num)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)
        print("~")
# } Driver Code Ends