# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        n=str(n)
        
        res=''
        
        for ch in n:
            if ch=='0':
                res+='5'
            else:
                res+=ch
        return int(res)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
# } Driver Code Ends