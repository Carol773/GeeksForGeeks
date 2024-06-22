class Solution:
    def ExtractNumber(self,sentence):
        #code here
        lst=sentence.split(' ')
        num=[-1]
        
        for digit in lst:
            if digit.isdigit() and '9' not in digit:
                num.append(int(digit))
                
        return max(num)


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends