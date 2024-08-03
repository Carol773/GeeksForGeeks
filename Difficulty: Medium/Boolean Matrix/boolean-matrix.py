#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    m=len(matrix)
    n=len(matrix[0])
    
    rows=[0]*m
    cols=[0]*n
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                rows[i]=1
                cols[j]=1
                
    for i in range(m):
        for j in range(n):
            if rows[i]==1 or cols[j]==1:
                matrix[i][j]=1
            
    
                
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends