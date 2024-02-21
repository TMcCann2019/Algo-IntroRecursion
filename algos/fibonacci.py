#iterative version
def fib_iter(n):
    first = 0
    second = 1

    if n == 1:
        return first
    elif n == 2:
        return second
    
    for i in range(3, n + 1):
        temp_second = second
        second = first + second
        first = temp_second
    return second

fibonacci = fib_iter(4)
#print(fibonacci)

#recursive version
def fib_recur(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)
        # return fib_recur(n - 2) + fib_recur(n-1) #will also work
    
fibonacci2 = fib_recur(40)
print(fibonacci2)