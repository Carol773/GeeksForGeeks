#User function Template for python3

class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        c=0
        
        
        
        for word in arr:
            prefix=s
            j=0
            while j<len(word) and j<len(prefix) and prefix[j]==word[j] and j!=k:
                j+=1
            
            prefix=prefix[:j]
            if len(prefix)==k:
               c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
        
        
# } Driver Code Ends