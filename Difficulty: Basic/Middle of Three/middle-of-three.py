#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        #code here
        lst=[]
        lst.append(A)
        lst.append(B)
        lst.append(C)
        lst.sort()
        
        return lst[1]

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends