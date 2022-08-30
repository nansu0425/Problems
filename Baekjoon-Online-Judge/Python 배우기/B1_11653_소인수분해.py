def print_prime_factors(n):
    d = 2
    while n >= d*d:
        if n%d==0:
            print(d)
            n //= d
        else:
            d += 1
    
    if n > 1:
        print(n)

n = int(input())
print_prime_factors(n)