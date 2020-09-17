class Student:
    def __init__(self,name:str, grades:dict):
        self.name = name
        self.grades = grades

    def get_grade(self):
        list_grade = []
        for grade in self.grades:
            list_grade.append(grade)
        print(f'Les notes de {self.name} sont {list_grade}')

    def general_grade(self):
        moy = 0
        for grade in self.grades:
            i =0
            if grade > 20 :
                print(f'{grade} est une note invalide')
                i+=1
            else:    
                moy +=grade        
        moyenne = moy // (len(self.grades)- i)
        print(f'{self.name} a une moyenne de {moyenne}')


