#User function Template for python3

class Solution:
    def minChange(self,S):
        # Code here
        l=len(set(S))
        return len(S)-l


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S = input()
        
        ob = Solution()
        print(ob.minChange(S))
# } Driver Code Ends