# Create a list of 10 elements if the list consist of duplicate values then remove those duplicate values
my_list = [1, 2, 3, 2, 4, 5, 6, 3, 7, 1]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("Original list:", my_list)
print("List with duplicates removed (order maintained):", unique_list)


# my_list = [1,2,3,4,2,3,6,7,8,6,7]
# unique_list = set(my_list)
# print(unique_list)