#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        str_num=''.join(str(x) for x in arr)
        num=int(str_num)+1
        num=str(num)
        num_str=''.join(x for x in num)
        return num_str
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends