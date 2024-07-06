#User function Template for python3

class Solution:
    def findSingle(self, n, arr):
        # code here
        freq={}
        
        for num in arr:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
                
        for key,val in freq.items():
            if val==1 or val%2!=0:
                return key


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends