
class Solution:
    def minDist(self, arr, n, x, y):
        arr_x=[]
        arr_y=[]
        
        for i in range(n):
            if arr[i]==x:
                arr_x.append(i)
            if arr[i]==y:
                arr_y.append(i)
                
        min_diff=float('inf')
        
        i=0
        j=0
        
        if len(arr_x)<=0 or len(arr_y)<=0:
            return-1
        else:
            while i<len(arr_x) and j<len(arr_y):
                diff=abs(arr_x[i]-arr_y[j])
                min_diff=min(min_diff,diff)
                
                if arr_x[i]<arr_y[j]:
                    i+=1
                else:
                    j+=1
            return min_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends