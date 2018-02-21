#!/bin/python2
# https://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english
# ^ excellent explanation of what's goind on here
import random
import math


def main():
    print("Hello, World!")
    # Generate our two random prime numbers between 3 and 1000
    # Generate g
    rando = random.randint(3, 1000)
    while is_prime(rando) is not True:
        rando+=1
    g = rando
    # Generate p
    rando = random.randint(3, 1000)
    # Double check we don't have the same value twice and also it's prime
    while (is_prime(rando) is not True) and (rando is not g):
        rando += 1
    p = rando
    print("Our shared values: g: " + str(g) + " p: " + str(p))
    # Generate a and b:
    rando = random.randint(3, 1000)
    while (rando is g) or (rando is p):
        rando = random.randint(3, 1000)
    a = rando
    rando = random.randint(3, 1000)
    while (rando is g) or (rando is p) or (rando is a):
        rando = random.randint(3, 1000)
    b =  rando
    print("Secret values: a:" + str(a) + " b: " + str(b))
    A = pow(g, a, p) # g^a mod p
    B = pow(g, b, p) # g^b mod p
    print("Calculated values: A: " + str(A) + " B: " + str(B))
    s_a = pow(A, b, p) # A^b mod p -> A's agreed value
    s_b = pow(B, a, p) # B^a mod p -> B's agreed value
    print("Our mutually agreed key: " + str(s_a) + " and other calculated: " + str(s_b))


# Found on Stack Overflow - there's no built-in Python method for generating primes easily
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

if __name__ == '__main__':
        main()

