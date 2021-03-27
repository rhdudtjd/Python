#factorial
def factorial(n):
    i = 0
    output = 1
    while n > i :
        output = output * (n - i)
        i += 1

    return output
     
num = int(input("숫자를 입력하세요 : "))

print(factorial(num))


#Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("숫자를 입력하세요 : "))

print(factorial(num))


#fibonacci
def fibonacci (n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

num = int(input("숫자를 입력하세요 : "))

print(fibonacci(num))

#memoization
dictionaty = {1:1, 2:2}

def fibonacci(n):
    if n in dictionaty:
        return dictionaty[n]
    else:
        output = fibonacci(n -1) + fibonacci(n - 2)
        dictionaty[n] = output
        return output

num = int(input("숫자를 입력하세요 : "))

print(fibonacci(num))