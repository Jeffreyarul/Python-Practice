class Student:
    
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    def letter_grade(self):
        av=self.average_grade()
        if av >=90 :
            return 'A'
        elif av >=80:
            return'B'
        elif av >=70:
            return 'C'
        elif av >=60:
            return 'D'
        else:
            return 'F'
        
s1=Student('jeff',[94,70,10,100])
s2=Student('jonathan',[100,100,100,100])
s3=Student('raj',[90,90,90,90])
l=[s1,s2,s3]
for i in l:
    i.add_grade(90)

for i in range(len(l)):
    s=l[i]
    print("the name of the student =",s.name)
    print("av.grades = ",s.average_grade())
    print("letter_grade = ",s.letter_grade())

    

                   