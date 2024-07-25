#User function Template for python3

class Solution:
    def encryptString(self, S):
        # code here
        res=[]
        c=1
        
        for i in range(1,len(S)):
            if S[i]==S[i-1]:
                c+=1
            else:
                res.append(hex(c)[2:].lower()+S[i-1])
                c=1
        res.append(hex(c)[2:].lower()+S[-1])
        encrypt=''.join(res[::-1])
        return encrypt
                
                


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.encryptString(S))
# } Driver Code Ends