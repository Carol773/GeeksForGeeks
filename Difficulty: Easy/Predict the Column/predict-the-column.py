#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        idx=-1
        maxele=0
        for i in range(N):
            c=0
            for j in range(N):
                if arr[j][i]==0:
                    c+=1
            if c>maxele:
                maxele=c
                idx=i
        return idx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends