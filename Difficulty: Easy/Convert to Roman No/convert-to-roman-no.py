#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        #Code here
        int_to_rom={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        
        res=''
        
        for value in sorted(int_to_rom.keys(),reverse=True):
            while n>=value:
                res+=int_to_rom[value]
                n-=value
        return res
        


#{ 
 # Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends