class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l =[]
        for i in range(1,numRows+1):
            l.append([1]*i)
        if numRows<3:
            return l
        x = [1,1]
        for i in range(2,len(l)):
            for j in range(1,len(l[i])-1):
                l[i][j]= x[j-1]+x[j]
            x = l[i]
        return l
            