class Bank:
  def __init__(self, id = 0 , balance = 0.0):
    self.id = id
    self.balance = balance
    
  def setID(self, ID):
    self.id = ID
    
  def setBalance(self, B):
    self.balance = B
  
  def getID(self):
    return self.id

  def getBalance(self):
    return self.balance 

bank1 = Bank()
bank1.setID(5)
bank1.setBalance(150.67)
print("Your bank id is: ")
print(bank1.getID())
print("Your bank balance is: ")
print(bank1.getBalance())
print()

class Retail:
  def __init__(self, des = "", UoH = 0, price = 0.0):
    self.description = des
    self.unitsOnHand = UoH
    self.price = price
    self.units = ["Shirts", "Pants", "Hats"]

  def decreaseUoH(self, decAmount = 0):
    self.unitsOnHand -= decAmount

  def getPrice(self):
    return self.price
purchase = Retail("Clothing Store", 15, 4.75)
print("These are the retail options:")
for i in purchase.units:
  print(i)
choice = input("Which option would you like? ")
numOfUnits = int(input("How many " + choice + " would you like? "))
purchase.decreaseUoH(numOfUnits)
decTax = 0.1
taxOfTotal = (purchase.price * numOfUnits) * decTax
total = (purchase.price * numOfUnits) + taxOfTotal
print("Your total is: ")
print(total)
print()

class Student():
  pass
  def findNetID(net, list):
    count = 0
    for i in list:
      count += 1
      if (i == net and count == 1):
        print(student1.name)
        print(student1.gpa)
      if(i == net and count == 2):
        print(student2.name)
        print(student2.gpa)
      if(i == net and count == 3):
        print(student3.name)
        print(student3.gpa)
      
student1 = Student()
student1.netID = 5288
student1.name = "John Smith"
student1.gpa = 4.0

student2 = Student()
student2.name = "Alice Jones"
student2.netID = 7964
student2.gpa = 3.5

student3 = Student()
student3.name = "Brandon Greene"
student3.netID = 2000
student3.gpa = 2.0

studentNetID = [student1.netID, student2.netID, student3.netID]
Student.findNetID(7964, studentNetID)