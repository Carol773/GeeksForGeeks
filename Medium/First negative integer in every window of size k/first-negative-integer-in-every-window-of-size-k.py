#User function Template for python3
from collections import deque

def printFirstNegativeInteger( A, N, K):
    # code here
    dq=deque()
    
    res=[]
    
    for i in range(K):
        if A[i]<0:
            dq.append(A[i])
            
    if dq:
        res.append(dq[0])
    else:
        res.append(0)
        
    for i in range(K,N):
        if A[i]<0:
            dq.append(A[i])
        if A[i-K]<0:
            dq.popleft()
        if dq:
            res.append(dq[0])
        else:
            res.append(0)
    return res
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends