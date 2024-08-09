
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        l=0
        h=len(arr)-1
        rm=float('inf')
        lm=float('-inf')
        while l<=h:
            mid=(l+h)//2
            num=arr[mid]
            
            if num==k:
                return num
            elif num<k:
                lm=num
                l=mid+1
            else:
                rm=num
                h=mid-1
        if rm-k<=k-lm:
            return rm
        else:
            return lm
            
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends