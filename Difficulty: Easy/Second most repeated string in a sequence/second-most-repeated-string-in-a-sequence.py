#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        freq={}
        array=[]
        for word in arr:
            if word not in freq:
                freq[word]=1
            else:
                freq[word]+=1
                
        for key,val in freq.items():
            array.append(val)
        array.sort(reverse=True)
        sec=array[1]
        for key,val in freq.items():
            if sec==val:
                return key


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends