#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        freq={}
        seen=set()
        
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
                
        for k,v in freq.items():
            seen.add(v)
            
        arr=list(seen)
        
        if len(arr)==1:
            return 1
        if len(arr)>2:
            return 0
        if len(arr)==2:
            min_freq=min(arr)
            max_freq=max(arr)
            
            if (list(freq.values()).count(min_freq)==1 and min_freq==1) or (list(freq.values()).count(max_freq)==1 and max_freq-min_freq==1):
                return 1
            return 0
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends