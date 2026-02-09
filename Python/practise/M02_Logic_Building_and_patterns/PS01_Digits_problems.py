'''#read a number from the user and count the digits..
s=int(input("Enter a number:"))
count=0
while s>0:
    s=s//10
    count=count+1
print("no.of digits:",count)
print(len(str(s)))
'''
'''#read the input from the user and sum the digits of the number
s=int(input("Enter a number:"))
sum=0
while s>0:
    k=s%10
    sum=sum+k
    s=s//10
print("Sum of digits:",sum)
'''
'''#sum of the digits in  a single line
s=int(input("Enter a number:"))
print("Sum of digits:",sum(map(int,str(s)))) 
'''
'''digital root sum'''

'''n=int(input("Enter a number:"))
even=odd=0
while n>0:
    if (n%2)==0:
        even+=1
    else:
        odd+=1
    n//=10
print(even,odd)'''

#take a number as a input and reverse the number
n=int(input())
rev=0
while n>0:
    k=n%10
    rev=rev*10+k
    n= n//10
print(rev)