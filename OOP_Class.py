class Employee():

    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self, first, last ,pay):
        self.first = first
        self.lsat = last
        self.pay = pay
        self.email = first +'.'+ last + '@company.com'

        Employee.num_of_employees += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.lsat)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay =emp_str.split('-')
        return cls(first, last, pay)

print(Employee.num_of_employees)
emp_elad = Employee('elad', 'adi', 50000)
print(Employee.num_of_employees)
emp_chani = Employee('chani', 'adi', 60000)
print(Employee.num_of_employees)

# print(emp_elad.email)
# print(emp_chani.email)
# print(emp_elad.fullName())
# print(emp_elad.raise_amount)
print(emp_elad.pay)
emp_elad.apply_raise()
print(emp_elad.pay)

emp_str1 = 'jhon-levy-7000' #classmethod
a = Employee.from_string(emp_str1)
print(a.email)
print(a.pay)