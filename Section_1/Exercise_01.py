"""
Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
"""
a = 0
b = 1
print(a)
while a < 1000:
    a = a + b
    print(a)
    b = a + b
    print(b)
