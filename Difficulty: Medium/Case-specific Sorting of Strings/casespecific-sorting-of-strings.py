#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        upp=[]
        low=[]
        res=''
        
        for i in range(len(s)):
            if s[i].isupper():
                upp.append(s[i])
            else:
                low.append(s[i])
        upp.sort()
        low.sort()
        upp=''.join(x for x in upp)
        low=''.join(x for x in low)
        
        u=0
        l=0
        for i in range(len(s)):
            if s[i].isupper() and u<len(upp):
                res+=upp[u]
                u+=1
            elif s[i].islower() and l<len(low):
                res+=low[l]
                l+=1
                
        if u<len(upp) or l<len(low):
            res+=upp[u:]
            res+=low[l:]
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends