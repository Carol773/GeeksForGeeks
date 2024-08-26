#User function Template for python3

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        c=0
        a=str(bin(a)[2:])
        b=str(bin(b)[2:])
        
        m=len(a)
        n=len(b)
        
        if m>n:
           b=b.zfill(m)
        else:
           a=a.zfill(n)
           

        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        return c
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends