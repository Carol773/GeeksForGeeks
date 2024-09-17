#User function Template for python3

class Solution:
    def addMinChar (self, str1):
        # code here 
        if str1==str1[::-1]:
            return 0
        c=0   
        l=0
        h=len(str1)-1
        
        while l<=h:
            if str1[l]!=str1[h]:
                c+=1
                h=len(str1)-1-c
                l=0
            else:
                l+=1
                h-=1
        return c
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends