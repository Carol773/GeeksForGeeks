#User function Template for python3
from collections import deque
class Queue:
    def __init__(self):
        self.q=deque()
        
    def enqueue(self,X):
        # code here
        self.q.append(X)
        
    def dequeue(self):
        # code here
        if self.q:
            return self.q.popleft()
        else:
            return -1


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends