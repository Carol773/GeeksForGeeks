#User function Template for python3

class Solution:
    def rotate(self, N, D):
        # code here
        binrep=bin(N)
        binrep=binrep[2:].zfill(16)
        D=D%16
        lrot=binrep[D:]+binrep[0:D]
        rrot=binrep[-D:]+binrep[0:-D]
        
        return int(lrot,2),int(rrot,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends