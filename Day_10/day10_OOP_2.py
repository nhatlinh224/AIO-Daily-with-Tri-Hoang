class Staff:
    def __init__(self, name, age, address, salary, total_time):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.total_time = total_time

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {
              self.address}, Salary: {self.salary}, Total Time: {self.total_time}")

    def calculate_bonus(self):
        if self.total_time >= 200:
            bonus = self.salary * 20
        elif self.total_time >= 100:
            bonus = self.salary * 10
        else:
            bonus = 0
        return bonus


# Test cases
staff1 = Staff("A", 30, "Address A", 30000000, 300)
staff2 = Staff("B", 25, "Address B", 5000000, 199)
staff3 = Staff("C", 28, "Address C", 10000000, 99)

staff1.show_info()
print(f"Bonus: {staff1.calculate_bonus()}")
print()

staff2.show_info()
print(f"Bonus: {staff2.calculate_bonus()}")
print()

staff3.show_info()
print(f"Bonus: {staff3.calculate_bonus()}")
