class Solution:
    def canSplit(self, arr):
        #code here
        left_sum=sum(arr)
        sumele=0
        
        
        for r in range(len(arr)):
            
            if sumele==left_sum:
                return 1
            sumele+=arr[r]
            left_sum-=arr[r]
            
        return 0
        
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends