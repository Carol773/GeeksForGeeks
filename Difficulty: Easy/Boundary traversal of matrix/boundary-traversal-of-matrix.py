#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        res=[]
        first_row=[]
        right_boundary=[]
        bottom_boundary=[]
        left_boundary=[]
        
        for i in range(n):
            for j in range(m):
                if i==0:
                    res.append(matrix[i][j])
                elif i==(n-1):
                    bottom_boundary.append(matrix[i][j])
                else:
                    if m-1!=0:
                        left_boundary.append(matrix[i][0])
                    right_boundary.append(matrix[i][m-1])
                    break
        bottom_boundary.reverse()
        left_boundary.reverse()
        
        res.extend(first_row)
        res.extend(right_boundary)
        res.extend(bottom_boundary)
        res.extend(left_boundary)
        
        return res
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends