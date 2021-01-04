from sympy import symbols, Eq, solve


# 1ST SOLUTION


x, y = symbols('x y')
equation1 = Eq(x + y - 5, 8)
equation2 = Eq(x - y + 3, 10)
print(solve((equation1, equation2), (x, y)))

# 2ND SOLUTION


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


def fraction_input(statement):
    l, m = shorten(tuple(map(int, input(statement).split("/"))))
    return l, m


# enter 2 numbers seperated by / e.g. 2/3
a = fraction_input("a = ")
b = fraction_input("b = ")
c = fraction_input("c = ")
d = fraction_input("d = ")
e = fraction_input("e = ")
f = fraction_input("f = ")

W = subtraction(multiplication(a, e), multiplication(d, b))
WX = subtraction(multiplication(b, f), multiplication(c, e))
WY = subtraction(multiplication(a, f), multiplication(c, d))

x = division(WX, W)
y = division(WY, W)

print(x)
print(y)
