class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate

    def compute_pay(self, hours):
        raise NotImplementedError("Not Implemented")

class DailyWorker(Worker):
    def compute_pay(self, days_worked):
        daily_pay = self.salary_rate * days_worked
        return daily_pay

class SalariedWorker(Worker):
    def compute_pay(self, _):
        weekly_pay = self.salary_rate * 40
        return weekly_pay

dailyworker = DailyWorker(name="Krishna", salary_rate=100)
salariedworker = SalariedWorker(name="Kishore", salary_rate=1200)

days_worked = 5
weekly_hours = 40

print(f"{dailyworker.name}'s weekly pay:  ₹{dailyworker.compute_pay(days_worked)}")
print(f"{salariedworker.name}'s weekly pay:  ₹{salariedworker.compute_pay(weekly_hours)}")
