from unicodedata import name
from src.musician import Musician
from src.manager import Manager

class Band:
    def __init__(self, name, musicians, manager):
        self.name = name
        self.musicians = musicians
        self.manager = manager

    def pay_salaries(self):
        return self.manager.pay_salaries(self.musicians)

    def calculate_payroll(self):
        return self.manager.calculate_payroll(self.musicians)
    
    def play(self):
        band_performance = ""
        for musician in self.musicians:
            band_performance += f"{musician.play()}\n"
        return band_performance
