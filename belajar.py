class Employee:
   
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)



emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp3 = Employee("Satrio", 200)
emp4 = Employee("Bayu", 3)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print ("Total Employee %d" % Employee.empCount)