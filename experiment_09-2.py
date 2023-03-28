# ii) Generate Fibonacci sequence up to 100 using recursion.

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print("Fibonacci sequence:")
for i in range(100):
    print(recur_fibo(i))