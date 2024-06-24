#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        l=0
        org=set()
        res=0
        
        for r in range(len(S)):
            while S[r] in org:
                org.remove(S[l])
                l+=1
            org.add(S[r])
            res=max(res,r-l+1)
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends