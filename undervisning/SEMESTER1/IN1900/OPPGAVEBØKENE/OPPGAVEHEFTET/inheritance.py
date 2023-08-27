class Mammal:
    def info(self):
        return f"I have hair"
    
    def identity_mammal(self):
        print("I am a mammal")
    
class Primate(Mammal):
    def info(self):
        return Mammal(self.info(self))

P1 = Primate()
print(P1)