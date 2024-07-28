#User function Template for python3

class Solution:

    def evenNumSubstring(self, S):
        # code here
        c=0
        
        for idx,num in enumerate(S):
            if num in "24680":
                c+=(idx+1)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.evenNumSubstring(S))

        
# } Driver Code Ends