#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        
        #code here
        if not head or not head.next:
            return 0
        slow=head
        fast=head
        c=0
        idx=0
        while slow:
            slow=slow.next
            c+=1
        if (c+1)%2==0:
            cur=head
            c=c//2
            while (c-1)!=idx and cur:
                cur=cur.next
                idx+=1
            cur.next=cur.next.next
        elif (c)%2==0:
            cur=head
            c=c//2
            while (c-1)!=idx and cur:
                cur=cur.next
                idx+=1
            cur.next=cur.next.next
        return head
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        obj = Solution();
        res=obj.deleteMid(ll.head)
        printList(res)
# } Driver Code Ends