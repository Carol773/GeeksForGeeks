#User function Template for python3

from fractions import Fraction
class Solution:
    def compareFrac (self, str):
        
        # code here
        
        a,b=str.split(",")
        b=b.strip(' ')
        na=Fraction(a)
        nb=Fraction(b)
        

        if na>nb:
            ans=a
        elif na<nb:
            ans=b
        else:
            ans="equal"
        return ans
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends