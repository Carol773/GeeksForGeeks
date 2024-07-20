#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        c=0
        sub_arr=0
        for num in arr:
            if num==0:
                c+=1
            else:
                sub_arr+=((c+1)*c)//2
                c=0
        sub_arr+=((c+1)*c)//2
        return sub_arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends