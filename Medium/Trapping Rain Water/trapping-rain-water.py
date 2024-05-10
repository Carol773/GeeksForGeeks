
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        if not arr:
            return 0
        l,r=0,n-1
        left,right=arr[l],arr[r]
        res=0
        while l<r:
            if left<right:
                l+=1
                left=max(left,arr[l])
                res+=left-arr[l]
            else:
                r-=1
                right=max(right,arr[r])
                res+=right-arr[r]
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends