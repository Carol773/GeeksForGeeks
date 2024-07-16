#User function Template for python3
class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        mod=1000000007
        prod=1
        
        for num in arr:
            prod*=(num)%mod
        return prod%mod
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        ans = obj.product(arr)
        print(ans)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends