#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here
        initial_sum=sum(Arr[:K])
        maxele=initial_sum
        for i in range(K,N):
            initial_sum+=Arr[i]-Arr[i-K]
            maxele=max(initial_sum,maxele)
        return maxele
            
            
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends