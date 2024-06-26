#User function Template for python3

class Solution:
    def countWords(self,List, n):
        #code here
        freq_count={}
        c=0
        
        for word in List:
            if word not in freq_count:
                freq_count[word]=1
            else:
                freq_count[word]+=1
                
        for key,val in freq_count.items():
            if val==2:
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
# } Driver Code Ends