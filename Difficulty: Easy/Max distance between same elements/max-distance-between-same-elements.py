class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        # Code here
        freq={}
        
        for i in range(n):
            if arr[i] not in freq:
                freq[arr[i]]=[i]
            else:
                freq[arr[i]].append(i)
        m=-10**7
        
        for i in freq.values():
            i.sort()
            m=max(m,i[-1]-i[0])
        return m



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends