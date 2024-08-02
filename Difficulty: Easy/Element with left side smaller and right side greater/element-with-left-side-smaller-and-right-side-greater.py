#User function Template for python3

class Solution:
    def findElement(self, arr):
        # code here
        for i in range(1,len(arr)-1):
            first=arr[:i]
            second=arr[i+1:]
            
            ans1=all(x<arr[i] for x in first)
            ans2=all(x>arr[i] for x in second)
            
            if ans1==True and ans2==True:
                return arr[i]
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1
        ob = Solution()
        ans = ob.findElement(arr)
        print(ans)
# } Driver Code Ends