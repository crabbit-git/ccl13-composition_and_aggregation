class Musician:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.bank = 0
    
    def get_salary(self):
        return self.salary
    
    def get_bank(self):
        return self.bank
    
    def add_money(self, salary):
        self.bank += salary
    
    def play(self):
        return f"{self.name} is performing"
