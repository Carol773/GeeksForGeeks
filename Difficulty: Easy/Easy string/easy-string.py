#User function Template for python3

class Solution:

    def transform(self, S):
        # code here
        S=S.lower()
        res=''
        c=0
        if len(S)==1:
            return str(c+1)+S
        for i in range(len(S)-1):
            if S[i]==S[i+1]:
                c+=1
            else:
                res+=str(c+1)+S[i]
                c=0
        res+=str(c+1)+S[i+1]
        return res
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.transform(S))
# } Driver Code Ends