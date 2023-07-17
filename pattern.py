# WAP to print or sort the pattern in ascending or descending order.

#Ascending order
print('List in Ascending order')
list1 = ["Apple","Orange", "Lemon","Pineapple","Mango"]
list2 = [5,2,3,1,4]

#Printing the above lists

list1.sort(reverse = True)
list2.sort(reverse = True)

print(list1)
print(list2)

#Descending order
print('\nList in Descending order')
list1 = ["Apple","Orange", "Lemon","Pineapple","Mango"]
list2 = [5,2,3,1,4]

#Printing the above lists

list1.sort()
list2.sort()

print(list1)
print(list2)
