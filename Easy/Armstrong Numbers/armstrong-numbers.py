#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        s=0
        n=str(n)
        
        for i in range(len(n)):
            s+=int(n[i])**3

        if s==int(n):
            return "Yes"
        else:
            return "No"
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends