import time

def recur_coundown_timer(n):
    if n==0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recur_coundown_timer(n-1)

def iter_countdown_timer(n):
    while n>0:
        print(n)
        time.sleep(1)
        n-=1
    print(n)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

z=3

#print(recur_coundown_timer(z))
print(factorial(z))
print(fibonacci(z))
