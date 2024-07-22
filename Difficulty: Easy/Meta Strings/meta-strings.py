#User function Template for python3
class Solution:
    def metaStrings(self, S1, S2):
        # code here
        c=0
        for i in range(len(S1)):
            if S1[i]!=S2[i]:
                c+=1
            if c>2 or S1[i] not in S2:
                return 0
        if c==2:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        obj = Solution()
        if obj.metaStrings(S1, S2):
            print(1)
        else:
            print(0)
# } Driver Code Ends