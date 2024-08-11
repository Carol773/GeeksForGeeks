#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        
        pair=[[car[i],fine[i]] for i in range(len(car))]
        sumele=0
        #print(pair)
        if date%2==0:
            for arr in pair:
                if arr[0]%2!=0:
                    sumele+=arr[1]
        else:
            for arr in pair:
                if arr[0]%2==0:
                    sumele+=arr[1]
        return sumele
        
        
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        date = int(input())
        car = [int(x) for x in input().strip().split()]
        fine = [int(x) for x in input().strip().split()]

        print(Solution().totalFine(date, car, fine))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends