#User function Template for python3

class Solution:
    def stringFilter(self, str):
        # code here
        new_s=[]
        res=''
        i=0
        while i<len(str):
            if str[i]=='b':
                i+=1
            elif str[i]=='a' and (i+1)<len(str) and str[i+1]=='c':
                i+=2
            else:
                new_s.append(str[i])
                i+=1
                
        res=''.join(x for x in new_s)
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.stringFilter(s)
        print(ans)
# } Driver Code Ends