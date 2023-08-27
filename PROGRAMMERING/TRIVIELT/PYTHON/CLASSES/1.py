class people:
    def __init__(self, first_name,surname, age, sex):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.sex = sex
    
    def __str__(self):
        return f"{self.first_name} {self.surname}"
    
    def f(self, age):
        return f"{str(self)} er {age-10} år eldre enn sara, som er 10 "


man1 = people("Tom", "banks", 69, "man")
woman1 = people("Sasha", "banks", 38, "woman")
print(str(man1))
print(woman1.f(69))
