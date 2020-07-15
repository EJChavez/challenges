# try to implement fibonacci number


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        c = a
        a = b
        b = c + b

for x in fib(21):
    print(x)



def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        c = a
        a = b
        b = c + b
    return result

print(fib2(21))