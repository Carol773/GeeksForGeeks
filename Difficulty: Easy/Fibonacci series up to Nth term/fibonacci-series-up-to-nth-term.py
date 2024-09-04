#User function Template for python3

class Solution:
    def series(self, n):
        lst=[]
        # Code here
        n1=0
        n2=1
        c=0
        
        if n==0:
            lst.append(n1)
            return lst
        elif n==1:
            lst.append(n1)
            lst.append(n2)
            return lst
        else:
            while c<=n:
                lst.append(n1)
                n3=(n1+n2)%1000000007
                n1=n2
                n2=n3
                c+=1
            return lst
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends