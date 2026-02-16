
'''
Armstrong Number: A number is called an Armstrong number if it is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
'''
'''Armstrong number:
input:153
output:Armstrong number

input:24  
output:Not an Armstrong number
'''
'''n=int(input())
count=len(str(n))
s=0
for digit in str(n):
    s=s+int(digit)**count   
print("Armstrong number" if s==n else "Not an Armstrong number")

strong number:
input:123
output:Not a strong number
Explanation: 1! + 2! + 3! = 9 which is not equal to 123'''

def factorial(n):
    if n<0:
        return "no factorial for -ve"
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
n=int(input())
s=0
for digit in str(n):
    s+=factorial(int(digit))
print("strong number" if s==n else "Not a strong number")


