#User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        c=0
        row=0
        maxc=0
        
        for i in range(N):
            j=0
            while j<N:
                if mat[i][j]==1:
                    c+=1
                j+=1
            if c>maxc:
                maxc=c
                row=i
            j=0
            c=0
        return row,maxc
            
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
# } Driver Code Ends