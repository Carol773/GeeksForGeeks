#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        m=len(matrix)
        n=len(matrix[0])
        lst=[]
        i=0
        j=0
        
        while i<m and j<n:
            for k in range(j,n):
                lst.append(matrix[i][k])
            i+=1
                
            for k in range(i,m):
                lst.append(matrix[k][n-1])
            n-=1
                
            if i<m:
                for k in range(n-1,j-1,-1):
                    lst.append(matrix[m-1][k])
                m-=1
                
            if j<n:
                for k in range(m-1,i-1,-1):
                    lst.append(matrix[k][j])
                j+=1
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends