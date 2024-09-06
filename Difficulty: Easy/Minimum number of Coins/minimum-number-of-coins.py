#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        money=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        lst=[]
        
        i=len(money)-1
        while i>=0:
            while N>=money[i]:
                N-=money[i]
                lst.append(money[i])
            else:
                i-=1
        return lst
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends