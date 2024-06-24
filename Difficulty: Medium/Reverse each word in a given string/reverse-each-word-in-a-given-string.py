#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        lst=s.split('.')
        nlst=[]
        for word in lst:
            nlst.append(word[::-1])
        
        res='.'.join(x for x in nlst)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends