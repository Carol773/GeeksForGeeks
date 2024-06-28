#User function Template for python3

class Solution:
    def arrangeString(self, s):
        # code here
        lst=[]
        num=[]
        num_sum=0
        for ch in s:
            if ch.isalpha():
                lst.append(ch)
            else:
                num.append(int(ch))
        
        lst.sort()        
        for nums in num:
            num_sum+=nums
        res=''.join(x for x in lst)
        
        if num_sum==0:
            return res
        else:
            ans=res+str(num_sum)
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends