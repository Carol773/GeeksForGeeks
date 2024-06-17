class Solution:
    def findExtra(self,n,a,b):
        #add code here
        freq_count={}
        
        for i in a:
            if i not in freq_count:
                freq_count[i]=1
            else:
                freq_count[i]+=1
                
        for i in b:
            if i not in freq_count:
                freq_count[i]=1
            else:
                freq_count[i]-=1
                
        for val,idx in freq_count.items():
            if idx!=0:
                return a.index(val)
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends