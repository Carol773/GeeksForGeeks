
#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
       m=len(matrix)
       lst=[]
       nlst=[]
       c=0
       
       for i in range(m):
           for j in range(m):
            lst.append(matrix[i][j])
            
       for i in range(0,len(lst),m):
           if c%2==0:
               nlst.extend(lst[i:i+m])
           else:
               new=lst[i:i+m]
               nlst.extend(new[::-1])
           c+=1
           
       return nlst
               


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends