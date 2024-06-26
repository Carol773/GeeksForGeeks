#User function Template for python3


class Solution:
    def minFlips(self, S):
        # Code here
        flip=0
        
        for i in range(len(S)):
            if i%2==0:
                if S[i]=='0':
                    flip+=1
            if i%2!=0:
                if S[i]=='1':
                    flip+=1
        c=min(flip,len(S)-flip)
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends