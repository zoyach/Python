'''a=int(input("enter table number: "))
b=int(input("enter the number to which table is to printed: "))
i=1
while i<=b:
    print(a,"x",i,"=",a*i)
    i=i+1'''

a=int(input("enter table number: "))
b=int(input("enter the number to which table is to printed: "))
i=1
for i in range(i,b+1):
     print(a,"x",i,"=",a*i)
