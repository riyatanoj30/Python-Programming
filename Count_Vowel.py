# Write a program to count the number of occurance of all vowels present in a string
str = input("Enter a String: ").lower()
# x = 'a' and 'e' and 'i' and 'o' and 'u'
vowels = "aeiou"  
#count = sum(str.count(v) for v in vowels)  
print("No. of vowels in the entered string is", sum(str.count(v) for v in vowels) )
