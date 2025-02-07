# Creating tuple
tuple_ds = ()
print(type(tuple_ds))  # Added print to display the type
tuple_ds = (1, 2, 3, 4, 5)
print(tuple_ds)
tuple_ds = (12,)
print(type(tuple_ds))  # Added print to display the type
print(tuple_ds)

# Accessing tuple
tuple_ds = (1, 2, 3, 4, 5, 'tuple_example', 5.55)
print(tuple_ds)
for t in tuple_ds:
    print(t)
print(tuple_ds)
print(tuple_ds[0])
print(tuple_ds[:])
print(tuple_ds[5][4])  # Accessing the 5th character of the string 'tuple_example'

# Appending to a tuple
tuple_ds = tuple_ds + (23, 24, 25)  # Adding elements
print(tuple_ds)

# tuple_ds[2] = 100  # This line is commented out since tuples are immutable

print(tuple_ds)
nestuple = (12, 14, 15, [50, 80, 70], "Good Afternoon")
print(nestuple)
nestuple[3][1] = 100  # Modifying the list inside the tuple
print(nestuple)

# Deleting a tuple
deltuple = (10, 20, 30, 40, 50)
print(deltuple)
del deltuple
# print(deltuple)  # This will cause an error because the tuple is deleted
