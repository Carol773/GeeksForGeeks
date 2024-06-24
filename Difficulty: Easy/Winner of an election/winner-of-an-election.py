#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        freq_count={}
        for char in arr:
            if char not in freq_count:
                freq_count[char]=1
            else:
                freq_count[char]+=1
        
        max_val=-1
        winner=''
        for key,val in freq_count.items():
            if val>max_val:
                max_val=val
                winner=key
            elif val==max_val and key<winner:
                max_val=val
                winner=key
        return winner,max_val
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends