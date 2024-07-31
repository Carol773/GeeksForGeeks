#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        prefix=arr[0]
        
        for word in arr[1:]:
            i=0
            while i<len(word) and i<len(prefix) and word[i]==prefix[i]:
                i+=1
            prefix=prefix[:i]
        if prefix:
            return prefix
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends