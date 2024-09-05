#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        min_cost=0
        max_cost=0
        
        i=0
        while N>0:
            min_cost+=candies[i]
            i+=1
            N-=(K+1)
        
        N=len(candies)   
        i=len(candies)-1
        while N>0:
            max_cost+=candies[i]
            i-=1
            N-=(K+1)
        
        return min_cost,max_cost


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends