
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        x=0
        y=0
        arr=[0]*26
        
        for c in s:
            arr[ord(c)-ord('a')]+=1
            
        for i in range(26):
            if arr[i]!=0:
                if arr[i]%2==0 and(i+1)%2==0:
                    x+=1
                elif arr[i]%2!=0 and (i+1)%2!=0:
                    y+=1
        
        if (x+y)%2==0:
            return "EVEN"
        else:
            return "ODD"
            
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends