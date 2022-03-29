class Manager:
    def __init__(self, name):
        self.name = name
        self.address = "666 Benevolent Street"

    def pay_salaries(self, musicians):
        for musician in musicians:
            musician.add_money(musician.salary)
    
    def calculate_payroll(self, musicians):
        total = 0
        for musician in musicians:
            total += musician.salary
        return total
