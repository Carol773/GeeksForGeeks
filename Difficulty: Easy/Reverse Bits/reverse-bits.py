#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        bin_rep=bin(x)
        bin_num=bin_rep[2:]
        
        bin_new=bin_num.zfill(32)
        
        bin_rev=bin_new[::-1]
        
        ans=int(bin_rev,2)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends