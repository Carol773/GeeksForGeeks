
# Helper class Geeks to implement 
# insert() and findFrequency()
class Geeks:
    
    # Function to insert element into the queue
    def insert(self, q, k):
        
        # Your code here
        # Just insert k in q and don't return anything
        q.append(k)
    
    # Function to find an element k
    def find(self, q, k):
        
        # Your code here
        # If k is in q return true else return false
        if k in q:
            return True
        else:
            return False
        
    
    # Function to delete the max element from queue
    def delete(self, q):

        # Your code here
        # Delete the max element from q. The priority queue property might be useful here
        if q:
            ele=max(q)
            q.remove(ele)
            return ele
            
        else:
            return -1
        


#{ 
 # Driver Code Starts
import heapq

# Driver class with driver code
if __name__ == '__main__':
    # Taking input using input() method
    testcase = int(input())
    
    while testcase > 0:
        # Priority Queue with comparator
        p_queue = []
        
        n = int(input())
        
        # Invoking object of Geeks class
        obj = Geeks()
        
        elements = list(map(int, input().split()))
        for i in range(n):
            obj.insert(p_queue, elements[i])
        
        # Taking total number of queries
        x = int(input())
        lst = list(map(int, input().split()))
        
        # If the element entered is present 
        # in the PriorityQueue then we print
        # "1" and delete the maximum element
        # else we print "-1"
        for i in range(x):
            k = lst[i]
            f = obj.find(p_queue, k)
            if f:
                print("1")
                print(obj.delete(p_queue))
            else:
                print("-1")
        
        testcase -= 1

# } Driver Code Ends