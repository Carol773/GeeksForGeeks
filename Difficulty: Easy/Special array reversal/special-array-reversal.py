#User function Template for python3

class Solution:
    def reverse(self, s):
        # code here
        lst=[]
        res=''
        
        for ch in s:
            if ch.isalpha():
                lst.append(ch)
                
        new_s=lst[::-1]
        
        j=0
        for i in range(len(s)):
            if s[i].isalpha():
                res+=new_s[j]
                j+=1
            else:
                res+=s[i]
        return res
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverse(s)
        print(ans)
# } Driver Code Ends