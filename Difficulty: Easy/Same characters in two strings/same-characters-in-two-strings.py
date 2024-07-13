#User function Template for python3

class Solution:

    def sameChar(self, A, B):
        # code here
        A=A.lower()
        B=B.lower()
        count=0
        
        for i in range(len(A)):
            if A[i]==B[i]:
                count+=1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        A = input().strip()
        B = input().strip()

        solObj = Solution()

        print(solObj.sameChar(A, B))

# } Driver Code Ends