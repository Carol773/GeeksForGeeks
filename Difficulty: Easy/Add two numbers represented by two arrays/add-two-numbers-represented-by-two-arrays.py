#User function Template for python3

class Solution:
    def calc_Sum (self, arr,  n, brr, m) : 
        #Complete the function
        num1=''.join(str(x) for x in arr)
        num2=''.join(str(x) for x in brr)
        
        res=int(num1)+int(num2)
        
        return res
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.calc_Sum(arr, n, brr, m)
    print(res)


# } Driver Code Ends