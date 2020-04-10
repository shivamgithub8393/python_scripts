## fibibonacci numbers: 0 1 1 2 3 5 8 13 21 34 ....

## Using lambda function 
n = int(input(""))
fib = [0,1]

list(map(lambda i: fib.append(fib[i-1] + fib[i-2]), range(2, n)))
print("Fibonacci numbers:" , fib)





## using list comprehension
n = int(input(""))
fib = [0,1]

[fib.append(fib[i-1] + fib[i-2]) for i in range(2,n)]
print("Fibonacci numbers:" , fib)





## using loop 
n = int(input(""))
fib = [0,1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print("Fibonacci numbers:" , fib)