#User function Template for python3

class Solution:
    def isPatternPresent(self, S , P):
        # code here 
        if (P[0]=='^') and (S[0:(len(P)-1)] in P):
            return 1
        elif (P[len(P)-1]=='$') and (S[(len(S)-len(P)+1):len(S)] in P):
            return 1
        elif P in S:
            return 1
        else:
            return 0
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        P=input()
        S=input()
        
        ob = Solution()
        print(ob.isPatternPresent(S,P))
# } Driver Code Ends