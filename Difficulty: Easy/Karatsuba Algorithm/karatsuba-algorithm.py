#User function Template for python3

class Solution:
    def karatsubaAlgo(self, A , B):
        # code here 
        A=int(A,2)
        B=int(B,2)
        prod=A*B
        return prod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B = map(str,input().split())
        
        ob = Solution()
        print(ob.karatsubaAlgo(A,B))
# } Driver Code Ends