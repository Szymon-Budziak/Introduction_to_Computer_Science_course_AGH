"""
Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2, 3, 5.
Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
od 1 do N włącznie.
"""
n = 120
starting_number = 120
i = 1

while n > 0:
    if n == 1:
        print(n)
        break
    else:
        while n % 2 == 0:
            n = n / 2
            if n == 1:
                print(starting_number)
        else:
            while n % 3 == 0:
                n = n / 3
                if n == 1:
                    print(starting_number)
            else:
                while n % 5 == 0:
                    n = n / 5
                    if n == 1:
                        print(starting_number)
                else:
                    n = 120 - i
                    starting_number -= 1
                    i += 1
