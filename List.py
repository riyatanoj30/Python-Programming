# create a list of 20 elements and display it in reverse order
rev = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Before Reverese: ", rev)
print("After Reverese: ", rev[::-1])

# create 2 list with 5 elements each combine both and display
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,0]
lst1.extend(lst2)
print("Merge = ",lst1)

# consider the list with following elements [20,30,40,20,50] find and replace the first occurence of 20 with 10
numbers = [20, 30, 40, 20, 50]
numbers[numbers.index(20)] = 10
print(numbers) 

# create a list which consist of course name for MCA sem-2, at index 5 substitute the course name with pre placement training
mca = ["pyhton", "DSA", "SE", "PRofile Building", "coding tool kit", "Javascript"]
mca[5] = "placement training"
print(mca)

# create a list of 10 numbers and display the sum of the numbers
lst3 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in lst3:
    sum += i
print(sum)