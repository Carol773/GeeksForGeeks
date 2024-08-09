#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        work=[]
        a=[]
        for i in range(n):
            a=[start[i],end[i]]
            work.append(a)
            a=[]
        work.sort(key=lambda x:x[1])
        c=1
        j=work[0][1]
        for i in range(1,len(work)):
            if j<work[i][0]:
                c+=1
                j=work[i][1]
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends