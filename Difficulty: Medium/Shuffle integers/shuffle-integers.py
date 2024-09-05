class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        mid=n//2
        
        alst=[]
        blst=[]
        
        for i in range(mid):
            alst.append(arr[i])
        
        for i in range(mid,n):
            blst.append(arr[i])

        i=0
        j=0
        p=0
        
        while (i<len(alst) and p<len(arr)) or (j<len(blst) and p<len(arr)):
            if p%2==0:
                arr[p]=alst[i]
                i+=1
            else:
                arr[p]=blst[j]
                j+=1
            p+=1
        return arr
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends