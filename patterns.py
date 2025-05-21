print("/nleft sided pyramid")
for i in range(7):
   x='*' * i
   print (f'{x:<10}')

print("/nnormal pyramid")
for i in range(1,7):
   x='*' * (2*i-1)
   print (f'{x:10}')

print("/nright sided pyramid")
for i in range(7):
   x='*' *(i+1)
   print (f'{x:>10}')

print("L Shape\n")
n = int(input("Enter height of L shape: "))

for i in range(n):
    if i == n - 1:
        print('*' * n)  
    else:
        print('*')
        


