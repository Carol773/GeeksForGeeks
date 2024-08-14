#User function Template for python3
import itertools

class Solution:
    def find_permutation(self, S):
        # Code here
        perm=[''.join(p) for p in itertools.permutations(S)]
        set_perm=set(perm)
        res=list(set_perm)
        return res
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends