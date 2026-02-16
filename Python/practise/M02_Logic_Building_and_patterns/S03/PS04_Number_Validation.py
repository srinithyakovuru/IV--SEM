
'''
Armstrong Number: A number is called an Armstrong number if it is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
'''
'''Armstrong number:
input:153
output:Armstrong number

input:24
output:Not an Armstrong number
'''
n=int(input())
count=len(str(n))
s=0
for i in str(n):
    s=s+int(i)**count
print("Armstrong number" if s==n else "Not an Armstrong number")

