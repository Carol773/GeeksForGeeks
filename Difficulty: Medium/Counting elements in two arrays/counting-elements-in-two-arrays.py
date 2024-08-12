#User function Template for python3

class Solution:
    def BinarySearch(self,arr,x):
        l=0
        n=len(arr)
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]<=x:
                l=mid+1
            else:
                r=mid-1
        if l<n and arr[l]<=x:
            return l+1
        return l
    
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        
        arr2.sort()
        res=[]
        
        for i in range(n1):
            res.append(self.BinarySearch(arr2,arr1[i]))
        return res
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]
    
        res = Solution().countEleLessThanOrEqual(arr1,n1,arr2,n2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends