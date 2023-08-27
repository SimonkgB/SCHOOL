class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, new_name):
        self.name = new_name
    
    def change_age(self, new_age):
        self.age = new_age

    def change_gender(self, new_gender):
        self.gender = new_gender
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"

p1 = Person("John", 55, "male")
print(p1)
p1.change_name("T-33")
p1.change_gender("attack hellicopter")
print(p1)

"""
Terminal> python.exe class_people.py
John, 55, male
T-33, 55, attack hellicopter
"""