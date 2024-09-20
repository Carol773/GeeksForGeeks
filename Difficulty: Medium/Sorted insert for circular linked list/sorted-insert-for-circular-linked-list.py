#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        #code here
        newnode=Node(data)
        
        if not head:
            newnode.next=newnode
            return newnode
            
        cur=head
        
        if data<=head.data:
            while cur.next!=head:
                cur=cur.next
            cur.next=newnode
            newnode.next=head
            return newnode
            
     
        while cur.next!=head and cur.next.data<data:
            cur=cur.next
        newnode.next=cur.next
        cur.next=newnode
        return head


#{ 
 # Driver Code Starts
# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(head):
    if head is None:
        return

    current = head
    while True:
        print(current.data, end=" ")
        current = current.next
        if current == head:
            break
    print()


# Main function
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        # Read input for each test case
        arr = list(map(int, input().split()))
        x = int(input())  # Value to insert

        # Initialize the linked list
        head = Node(arr[0])
        tail = head

        # Create the circular linked list from the array
        for num in arr[1:]:
            tail.next = Node(num)
            tail = tail.next
        tail.next = head  # Make the list circular

        # Create an instance of Solution class
        ob = Solution()

        # Insert node in the sorted circular linked list and get the updated head
        ans = ob.sortedInsert(head, x)

        # Print the updated linked list
        printList(ans)

# } Driver Code Ends