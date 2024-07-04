#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compare(head1, head2):
    #return 1/-1/0
    cur1=head1
    cur2=head2
    string1=''
    string2=''
    
    while cur1!=None:
        string1+=cur1.data
        cur1=cur1.next
        
    while cur2!=None:
        string2+=cur2.data
        cur2=cur2.next
        
    if string1==string2:
        return 0
    elif string1>string2:
        return 1
    else:
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

        
    

        
def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=input().split()
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        n2=int(input())
        arr2=input().split()
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        print(compare(ll1.head,ll2.head))
        
    
    
# } Driver Code Ends