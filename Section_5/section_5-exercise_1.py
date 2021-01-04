def addition(a, b):
    return shorten((a[0]*b[1] + b[0]*a[1], a[1]*b[1]))


def subtraction(a, b):
    return shorten((a[0]*b[1]-b[0]*a[1], a[1]*b[1]))


def multiplication(a, b):
    return shorten((a[0]*b[0], a[1]*b[1]))


def division(a, b):
    return shorten((a[0]*b[1], a[1]*b[0]))


def power(a, n):
    return shorten((a[0]**n, a[1]**n))


def equal(a, b):
    return a[0]*b[1] == a[1]*b[0]


def shorten(n):
    def GCD(n1, n2):
        n1 = abs(n1)
        n2 = abs(n2)
        while n2 != 0:
            n2, n1 = n1 % n2, n2
        return n1
    result = GCD(n[0], n[1])
    return n[0]//result, n[1]//result


# enter numbers seperated by / e.g. 2/3
def fraction_input(statement):
    l, m = shorten(tuple(map(int, input(statement).split("/"))))
    return l, m
