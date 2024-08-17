#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        
        
        for it in range(r):
            res=''
            for i in range(n//2+1):
                if s[i]=='1':
                    res+='10'
                    
                if s[i]=='0':
                    res+='01'
                    
            s=res

        return s[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends