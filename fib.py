def fib(n,k):
    ralive=[1,1+k]
    for i in range(n-2):
        offspring= k * ralive[-2]
        ralive.append(offspring+ralive[-1])
    return ralive

print(fib(29, 4)[-2])