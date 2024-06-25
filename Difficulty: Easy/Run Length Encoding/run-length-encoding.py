
class Solution:
    def encode(self, s : str) -> str:
        # code here
        res=''
        c=0
        for i in range(len(s)-1):
            if s[i+1]==s[i]:
                c+=1
            else:
                res+=s[i]+str(c+1)
                c=0
        res+=s[i+1]+str(c+1)
        return res
            
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.encode(s)
        
        print(res)
        

# } Driver Code Ends