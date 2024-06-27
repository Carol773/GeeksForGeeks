#User function Template for python3
class Solution:
	def printString(self, S, ch, count):
		# code here
		c=0
		if count==0:
		    return S
		for i in range(len(S)):
		    if S[i]==ch:
		        c+=1
		        if c==count:
		            if S[i+1:]!='':
		                return S[i+1:]
		            else:
		                return 'Empty string'
		return 'Empty string'
		



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ch = input()[0]
		count = int(input())
		ob = Solution()	
		answer = ob.printString(s,ch,count)
		
		print(answer)


# } Driver Code Ends