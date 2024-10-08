'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
    
        sum_petrol=0
        sum_dist=0
        start=0
        sum1=0
        
        for i in range(n):
            sum_petrol+=lis[i][0]
            sum_dist+=lis[i][1]
            sum1+=lis[i][0]-lis[i][1]
            
            if sum1<0:
                sum1=0
                start=i+1
                
        if sum_petrol<sum_dist:
            return -1
        else:
            return start
    
            
                


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends