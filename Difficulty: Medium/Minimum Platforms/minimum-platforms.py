#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        c=1
        i=1
        j=0
        arr.sort()
        dep.sort()
        min_plat=1
        
        while i<n and j<n:
            if arr[i]<=dep[j]:
                c+=1
                i+=1
            else:
                c-=1
                j+=1
            min_plat=max(c,min_plat)
        return min_plat
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends