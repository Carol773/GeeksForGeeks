#User function Template for python3



def maxArea(A,le):
    #code here
    l=0
    r=le-1
    ans=0
    
    while l<r:
        temp=min(A[l],A[r])*(r-l)
        ans=max(ans,temp)
        if A[l]<A[r]:
            l+=1
        else:
            r-=1
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends