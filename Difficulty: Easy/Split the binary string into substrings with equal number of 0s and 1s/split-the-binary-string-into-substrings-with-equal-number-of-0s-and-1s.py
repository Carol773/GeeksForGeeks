#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        c=0
        z=0
        i=0
        
        while i<len(str):
            if str[i]=='0':
                z+=1
            else:
                z-=1
            if z==0:
                c+=1
            i+=1
        if z==0:
            return c
        else:
            return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends