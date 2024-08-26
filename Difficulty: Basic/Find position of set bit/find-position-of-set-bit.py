#User function Template for python3

class Solution:
    def findPosition(self, N):
        # code here 
        num=bin(N)[2:]
        n=len(num)
        
        c=num.count('1')
        
        if c==1:
            return n-(num.index('1'))
                
        return -1
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends