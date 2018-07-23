#https://projecteuler.net/problem=2
#Each new term in the Fibonacci sequence is generated 
#by adding the previous two terms. By starting with 1 
#and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence 
#whose values do not exceed four million, find the sum
#of the even-valued terms.
fibnumbers = (1,2)
fib1 = 1
fib2 = 2
sumfibeven = 0


def sumFibeven(fib1, fib2, sumfibeven):
    fib3 = fib1 + fib2
    if(fib1 % 2 == 0):
        sumfibeven = sumfibeven + fib1
    if(fib2 % 2 == 0):
        sumfibeven = sumfibeven + fib2
    fib1 = fib2
    fib2 = fib3
    return fib1, fib2, sumfibeven


if fib1 <= 4000000 and fib2<= 4000000:
    print sumFibeven(fib1, fib2, sumfibeven)
else:
    print sumfibeven