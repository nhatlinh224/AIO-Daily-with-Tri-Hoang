class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Employee(Person):
    def __init__(self, name, phone, annual_salary, year_of_starting_work):
        super().__init__(name, phone)
        self.annual_salary = annual_salary
        self.year_of_starting_work = year_of_starting_work


class StackEmployee:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, obj):
        if self.is_full():
            raise Exception("Stack is full")
        self.stack.append(obj)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]


# Testing the StackEmployee class with capacity of 5
stack = StackEmployee(5)

# Create some Employee objects
emp1 = Employee("Alice", "123456789", 50000, 2015)
emp2 = Employee("Bob", "987654321", 60000, 2016)
emp3 = Employee("Charlie", "555666777", 70000, 2017)
emp4 = Employee("David", "111222333", 80000, 2018)
emp5 = Employee("Eve", "444555666", 90000, 2019)
emp6 = Employee("Frank", "777888999", 100000, 2020)

# Push employees onto the stack
stack.push(emp1)
stack.push(emp2)
stack.push(emp3)
stack.push(emp4)
stack.push(emp5)

# This push should raise an exception as the stack is full
try:
    stack.push(emp6)
except Exception as e:
    print(e)

# Check the top of the stack
print(stack.top().name)

# Pop an employee from the stack
stack.pop()

# Check the top of the stack again
print(stack.top().name)
