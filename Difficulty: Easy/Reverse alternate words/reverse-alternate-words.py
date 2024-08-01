#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        # code here
        lst=Str.split()
        nlst=[]
        i=0
        
        while i<len(lst):
            if i%2==0:
                nlst.append(lst[i])
            else:
                word=lst[i]
                new=word[::-1]
                nlst.append(new)
            i+=1
        res=' '.join(x for x in nlst)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends