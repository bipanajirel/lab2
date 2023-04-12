#Declare and initialize a list with the name “myNumbers”.
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#iterate through the list elements one by one and print it on the console.
print("List of numbers:")
for num in Numbers:
    print(num)

#Find and print all the elements from the list that are greater than 5.
greater_than_5 = []
for num in Numbers:
    if num > 5:
        greater_than_5.append(num)
print("List of numbers that are larger than 5:")
print(greater_than_5)