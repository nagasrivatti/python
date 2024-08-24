arr=[]
n=int(input("n:"))
for n in range(2,n+1):
        if n>0:
            is_prime=True
            for i in range(2,n):
                if n%i==0:
                    is_prime=False
                    break
        if is_prime:
            arr.append(n)
print(arr)
