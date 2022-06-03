animals = ["cat", "dog", "elephant", "fox", ["mouse", "bird", "beetle"]]
newlist = animals
print(newlist)
newlist[4][0] = ["caterpillar", "butterfly"]
print(newlist)
print(animals)

print ()
names = ["Kerry", "Thomas", "Marina", "Kevin", "Jose", "Gina", "Josephine"]
print("Original list: ")
print (names)
def onlyJK(list):
  JKnames = []
  length = len(list)
  for i in range(length):
    if(list[i][0] == "J" or list[i][0] == "K"):
      JKnames.append(list[i])
  print(JKnames)
print()
print("New list: ")
onlyJK(names)
print()

numbers = [1, 1, 1, 2, 2, 3, 4, 4]
print("Original list: ")
print(numbers)
def removeDups(list):
  noDupes = []
  for i in list:
    if i not in noDupes:
      noDupes.append(i)
  print (noDupes)
print ()
print("New list: ")
removeDups(numbers)