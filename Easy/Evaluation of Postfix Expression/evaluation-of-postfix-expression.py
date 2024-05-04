#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        stack=[]
        
        for i in range(len(S)):
            if S[i].isdigit():
                stack.append(S[i])
            else:
                if len(stack)>=2:
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    if S[i]=='+':
                        res=op1+op2
                    elif S[i]=='-':
                        res=op1-op2
                    elif S[i]=='*':
                        res=op1*op2
                    elif S[i]=='/':
                        res=op1//op2
                    stack.append(res)
        return stack[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends