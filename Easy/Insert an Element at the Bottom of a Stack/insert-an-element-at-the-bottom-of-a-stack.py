#User function Template for python3
class Solution:
    def insertAtBottom(self,st,x):
        # code here
        lst=[]
        lst.append(x)
        st=' '.join(str(x) for x in st)
        lst.append(st)
        return lst


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends