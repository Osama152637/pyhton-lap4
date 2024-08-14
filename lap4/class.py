class Human:
    count = 0
    def __init__(self, Fname, Lname, age, gender, favorite_food):
        self.Fname = Fname
        self.Lname = Lname
        self.age = age
        self.gender = gender
        self.food = favorite_food
        Human.count+=1
    
    def full_name(self):
        return f"{self.Fname} {self.Lname}"
    def introducing(self):
        return f"Hello my name is {self.Fname} i'm {self.age} years old"
    def welcoming(self):
        if self.gender == 'male':
            return f"Welcom Mr {self.Fname}"
        elif self.gender == 'female':
            return f"Welcome Miss {self.Fname}"
        else:
            return f"Welcome {self.Fname}"
    def eating(self):
        if self.gender == 'male':
            return f"Mr {self.Fname} favorite food is  {self.food}"
        elif self.gender == 'female':
            return f"Miss {self.Fname} favorite food is  {self.food}"
        else:
            return f"{self.Fname} favorite food is  {self.food}"

Human1 = Human('Osama', 'Selem', 26, 'male', 'Pasta with white sauce and chicken streps')
Human2 = Human('Ahmed', 'Nabil', 25, 'male', 'pizza')
Human3 = Human('Nirmen', 'Abd El-Nabi', 25, 'female', 'mhshy')
Human4 = Human('Mohmed', 'Emad', 24, 'male', 'Grand Tower')

print(Human1.full_name())
print(Human2.introducing())
print(Human3.welcoming())
print(Human2.welcoming())
print(Human4.eating())
print(Human1.eating())
print(Human3.eating())



class Employee:
    count = 0
    def __init__(self, Fname, Lname, age, gender, favorite_food):
        self.Fname = Fname
        self.Lname = Lname
        self.age = age
        self.gender = gender
        self.food = favorite_food
        Employee.count+=1
    
    def full_name(self):
        return f"{self.Fname} {self.Lname}"
    def introducing(self):
        return f"Hello my name is {self.Fname} i'm {self.age} years old"
    def welcoming(self):
        if self.gender == 'male':
            return f"Welcom Mr {self.Fname}"
        elif self.gender == 'female':
            return f"Welcome Miss {self.Fname}"
        else:
            return f"Welcome {self.Fname}"
    def eating(self):
        if self.gender == 'male':
            return f"Mr {self.Fname} favorite food is  {self.food}"
        elif self.gender == 'female':
            return f"Miss {self.Fname} favorite food is  {self.food}"
        else:
            return f"{self.Fname} favorite food is  {self.food}"

Employee1 = Employee('Osama', 'Selem', 26, 'male', 'Pasta with white sauce and chicken streps')
Employee2 = Employee('Ahmed', 'Nabil', 25, 'male', 'pizza')
Employee3 = Employee('Nirmen', 'Abd El-Nabi', 25, 'female', 'mhshy')
Employee4 = Employee('Mohmed', 'Emad', 24, 'male', 'Grand Tower')

print(Employee1.full_name())
print(Employee2.introducing())
print(Employee3.welcoming())
print(Employee2.welcoming())
print(Employee4.eating())
print(Employee1.eating())
print(Employee3.eating())