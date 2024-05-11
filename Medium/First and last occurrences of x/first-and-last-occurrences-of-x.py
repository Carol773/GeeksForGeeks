#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        lst=[]
        
        # code here
        if x not in arr:
            return [-1,-1]
        else:
            idx=arr.index(x)
            lst.append(idx)
            freq={}
            for i in arr:
                if i not in freq:
                    freq[i]=1
                else:
                    freq[i]+=1
        
            for key,value in freq.items():
                if key==x:
                    lst.append(idx+value-1)
                    break
            return lst


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends