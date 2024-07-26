#User function Template for python3

class Solution:

    def fun(self, s):
        # code here
        
        lst=set()
        i=0
        
        while i<len(s)-1:
            sub=s[i:i+2]
            lst.add(sub)
            i+=1
        return len(lst)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.fun(s))
# } Driver Code Ends