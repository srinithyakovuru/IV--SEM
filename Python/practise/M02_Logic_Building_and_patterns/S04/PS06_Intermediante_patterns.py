

'''li=[1,2,3,4,5]
#output=[2,4,6,8,10]
res=[]
for i in li:
    res.append(i*2)
print(res)
'''
#['a','b','c'] ==>"abc"
'''li1=['a','b','c']
res=""
for ch in li1:
    res+=ch
print(res)
print("".join(li1))
'''

'''Intermediate patterns:
1.pyramid pattern
n=4
output:
         *
        * *
       * * *
      * * * *
       '''
#pyramid pattern
t=int(input())
for i in range(1,t+1):
    print(" "*(t-i)+"* "*i)


    