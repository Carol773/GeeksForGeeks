class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        c=0
        arr.sort()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if arr[i]+arr[j]+arr[k]<sum:
                    c+=(k-j)
                    j+=1
                elif arr[i]+arr[j]+arr[k]>=sum:
                    k-=1
                
        return c


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.countTriplets(n, k, a)
    print(ans)

# } Driver Code Ends