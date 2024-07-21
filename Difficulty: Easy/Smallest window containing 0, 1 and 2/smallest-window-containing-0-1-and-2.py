#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        zero=-1
        one=-1
        two=-1
        ans=9999999999
        
        for i in range(len(S)):
            if S[i]=="0":
                zero=i
            elif S[i]=="1":
                one=i
            else:
                two=i
            if (zero!=-1) and (one!=-1) and (two!=-1):
                max_idx=max(one,max(two,zero))
                min_idx=min(one,min(two,zero))
                ans=min(ans,(max_idx-min_idx+1))
        if ans==9999999999:
            return -1
        return ans
                
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends