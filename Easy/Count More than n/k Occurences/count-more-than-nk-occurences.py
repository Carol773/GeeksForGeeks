#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        freq_count={}
        c=0
        for i in arr:
            if i not in freq_count:
                freq_count[i]=1
            else:
                freq_count[i]+=1
        
        for key,val in freq_count.items():
            if val>(n//k):
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends