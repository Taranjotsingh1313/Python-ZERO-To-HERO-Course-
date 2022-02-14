#           0               1      2  3     4    5   
# list1 = ["CodeWithSingh","Youtube",2,2.45,True,[1,2,3,4,5]]
# print(list1)
# print(type(list1))
# print(len(list1))

''' ACCESS ITEMS IN LIST'''
# b = list1[0]
# b = list1[1]
# b = list1[5]
# print(b)
'''CHANGING ITEMS'''
# list2 = ["codewithsingh","youtube","Software engineer","Python developer"]
# print(list2)
# list2[0] = "CWS"
# print(list2)

'''SLICING LIST'''
list2 = ["codewithsingh","youtube","Software engineer","Python developer"]
b = list2[0:2]

# getting the length of the list
# print(len(b))
'''FUNCTION FOR RETURNING THE INDEX OF ITEM'''
# print(list2.index("youtube"))
'''APPENDING NEW ITEMS IN THE LIST'''
# print(list2)
# print("-----")
# list2.append("Python")
# list2.append(1)
print(list2)
'''REMOVING ITEM IN THE LIST'''
# list2.pop()
list2.pop(0)
print(list2)