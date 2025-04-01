class NumberOperations:
    def __init__(self, num):
        self.num = num
    def factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact *= i
        return fact
    def reverse_number(self):
        rev = 0
        temp = self.num
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        return rev
    def is_palindrome(self):
        return self.num == self.reverse_number()
num = int(input("Enter a number: "))
obj = NumberOperations(num)
print("Factorial:", obj.factorial())
print("Reverse:", obj.reverse_number())
print("Palindrome:", "Yes" if obj.is_palindrome() else "No")
