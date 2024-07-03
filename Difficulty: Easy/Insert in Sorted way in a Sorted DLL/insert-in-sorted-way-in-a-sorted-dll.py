#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

def sortedInsert(head, x):
    #code here
    temp=Node(x)
    temp.prev=temp.next=None
    if head is None:
        return temp
        
    if x<=head.data:
        temp.next=head
        head.prev=temp
        return temp
        
    cur=head
    
    
    
    
        
    while cur.next!=None and x>cur.data:
        cur=cur.next
        
    if cur.next is None and x>cur.data:
        cur.next=temp
        temp.prev=cur
    else:

        prevv = cur.prev
        prevv.next = temp
        temp.prev = prevv
        temp.next = cur
        cur.prev = temp
    return head
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


def displayList(head):
    pvs=None
    while head:
        print(head.data, end=' ')
        if head.prev !=pvs:
            print('prev pointer not connected')
        pvs = head
        head = head.next
        


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        dll.head=sortedInsert(dll.head, x)
        displayList(dll.head)
        print()




# } Driver Code Ends