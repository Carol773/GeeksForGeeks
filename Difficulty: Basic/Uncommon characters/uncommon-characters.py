#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        res=''
        A=list(set(A))
        B=list(set(B))
        
        for i in range(len(A)):
            if A[i] not in B:
                res+=A[i]
                
        for i in range(len(B)):
            if B[i] not in A:
                res+=B[i]
                
        res=sorted(res)
        ans=''.join(x for x in res)
        if ans=='':
            return -1
        else:
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends