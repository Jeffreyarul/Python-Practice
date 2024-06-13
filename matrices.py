class Matrix:
    def __init__(self,m):
        self.m=m
        self.row=len(self.m)
        self.col=len(self.m[0])

    def add_matrices(self,n):
        ans=[]
        for i in range(self.row):
            temp=[]
            for j in range(self.col):
                l=self.m[i][j]+n[i][j]
                temp.append(l)
            ans.append(temp)
        return ans

    def transpose(self):
        ans = []
        for i in range(self.col):
            temp=[]
            for j in range(self.row):
                temp.append(0)
            ans.append(temp)  
        for i in range(self.row):
            for j in range(self.col):
                ans[j][i]=self.m[i][j]
        self.m=ans.copy()

    def display(self):
        for i in self.m:
            print(i)

A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
n=[[1,2,3],[4,3,1],[7,6,5]]
result=A.add_matrices(n)
print(result)
A.transpose()
A.display()
v=100
print("gross salary=",v)