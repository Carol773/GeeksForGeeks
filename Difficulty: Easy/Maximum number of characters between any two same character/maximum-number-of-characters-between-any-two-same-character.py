#User function Template for python3

class Solution:

    def maxChars(self, s):
        # code here
        
        freq={}
        max_dist=-1
        
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=i
            else:
                max_dist=max(max_dist,i-freq[s[i]]-1)
        return max_dist
            
        '''s.lower()
        max_dist=-1

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    max_dist=max(max_dist,j-i-1)
        return max_dist'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.maxChars(s)

        print(ans)

# } Driver Code Ends