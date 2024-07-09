#User function Template for python3

def deleteElement (arr, n, k) : 
    #Complete the function
    stack=[]
    stack.append(arr[0])
    for i in range(1,n):
        while stack!=[] and stack[-1]<arr[i] and k>0:
            stack.pop()
            k-=1
        stack.append(arr[i])

        
        
    return stack
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = deleteElement(arr, n, k)
    print(*ans)
# } Driver Code Ends