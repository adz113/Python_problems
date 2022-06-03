problem1 = "An electronics company sells routers that cost $109.99.  Assume tax is 12%.  Print the total price of 5 routers."
print (problem1)
router_cost = 109.99
tax = 0.12
numOfRouters = 5
router_tax = (router_cost*numOfRouters)*tax
total_price = (router_cost*numOfRouters)+ router_cost
print ("The price of 5 routers is: ", total_price)

print()
problem2 = "Write a program that asks the user for his or her score on an exam.  Next print the students grade where A = 90 to 100, B = 80-89, C = 70 – 79, D = 60-69, F is below 60."
print (problem2)
string_score = input("What is your exam score? ")
score = int(string_score)
if score >= 90: grade = "A"
elif score >= 80 and score < 90: grade = "B"
elif score >= 70 and score < 80: grade = "C"
elif score >= 60 and score < 70: grade = "D"
else:
  grade = "F"
print ("Your grade is: ", grade)

print ()
problem3 = "Write a function that calculates the tip for a meal. The user can choose the percentage of tip they wish to give.  Show that it works by calculating an 18% tip for a meal that costs 45.89."
print (problem3)
meal_cost = 45.89
string_tip = input("What percentage of tip do you wish to give? ")
int_tip = int(string_tip)
dec_tip = int_tip/100
calculated_tip = meal_cost*dec_tip
print ("Tip: ", calculated_tip)

print ()
problem4 = "Given a list of numbers [2,4,6,8,10,12,14], write a function that goes through the list and multiplies each number by 5.  Test your program with a list of even numbers from 2 to 14."
print (problem4)
import array as arr
a = arr.array('i', [2, 4, 6, 8, 10, 12, 14])
print("New List: ", end=" ")
for i in range(0,7):
  print (a[i]*5, end=" ")
print()

print()
problem5 = "Write a Python function that accepts three arguments: an array, the size of the array, and a number n.  Assume the array contains integers.  The function should display all integers in the array that are greater than the number n.  Test your function."
print (problem5)
array = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
size = 9
n = 3
def isGreater(array, size, n):
  for element in array:
    if n < element: print(element)
print ("Array is: [1, 2, 3, 4, 5, 6, 7, 8, 9] and n = 3")
print ("The numbers in the array that are greater than n are: ")
isGreater(array, size, n)
