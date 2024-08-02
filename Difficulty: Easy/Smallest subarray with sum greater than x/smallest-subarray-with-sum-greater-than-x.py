class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here
        
        sumele=0
        l=0
        min_idx=float('inf')
        
        for r in range(len(arr)):
            sumele+=arr[r]
            while sumele>x:
                min_idx=min(min_idx,r-l+1)
                sumele-=arr[l]
                l+=1
                
        if min_idx!=float('inf'):
            return min_idx
        else:
            return 0
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends