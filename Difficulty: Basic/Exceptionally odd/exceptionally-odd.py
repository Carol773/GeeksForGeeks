#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        freq={}
        
        for num in arr:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
                
                
        for k,v in freq.items():
            if v%2!=0:
                return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends