#User function Template for python3

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        o=0
        c=0
        res=-1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                o+=1
            else:
                c+=1
            if o==1:
                res=len(s)-(o+c)
            
                return res
        return res
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        s = input()
        ob = Solution()
        print(ob.lastIndex(s))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends