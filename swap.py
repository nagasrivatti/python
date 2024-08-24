#with using third variable
a=int(input("a:"))
b=int(input("b:"))
print(f"befor {a},{b}")
c=a
a=b
b=c
print(f"after",a,b)


#without using third variable
a=int(input("a:"))
b=int(input("b:"))
print(f"befor {a} {b}")
a=a+b
b=a-b
a=a-b
print(f"after",a,b)
