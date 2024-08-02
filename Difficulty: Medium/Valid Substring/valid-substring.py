#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        stack=[]
        stack.append(-1)
        res=0
        
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                res=max(res,i-stack[-1])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends