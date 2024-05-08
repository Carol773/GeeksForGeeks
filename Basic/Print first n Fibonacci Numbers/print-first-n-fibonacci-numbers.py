#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        lst=[]
        count=0
        n1=1
        n2=1
        if n==1:
            lst.append(n1)
            return lst
        elif n==2:
            lst.append(n1)
            lst.append(n2)
            return lst
        else:
            while count<n:
                lst.append(n1)
                n3=n1+n2
                n1=n2
                n2=n3
                count+=1
            return lst
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends