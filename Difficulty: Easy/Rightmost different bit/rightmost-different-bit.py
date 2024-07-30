#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




    
# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        bin_m=bin(m)[2:]
        bin_n=bin(n)[2:]
        
        

        l=max(len(bin_m),len(bin_n))
        bin_m='0'*(l-len(bin_m))+bin_m
        bin_n='0'*(l-len(bin_n))+bin_n
        
        i=len(bin_m)-1
        
        
        bin1=bin_m[::-1]
        bin2=bin_n[::-1]
        
        for i in range(l):
            if bin1[i]!=bin2[i]:
                return i+1
        return -1

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends