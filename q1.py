#!/bin/python2
# something something GPL v3
# Q1: 4 points max: Implement a fully functional knapsack crypto system:
# knapsack( int bits, int m, int n) should create a knapsack system for
# the given number of bits and the given values of m and n.
# (The example given in textbook has 8 bits).
# NOTE: Given m and n must be coprime


import argparse
import fractions
import random

def main():
    print("NOTE: Given numbers need to be greater than the sum of the napsack, so give large numbers")
    print("NOTE: m and n must be coprime! Run coprimes.py to generate a coprime")
    parser = argparse.ArgumentParser(description='USAGE: q1.py int bits, int m, int n')
    parser.add_argument('bits', metavar='bits', type=int, nargs=1)
    parser.add_argument('m', metavar='M', type=int, nargs=1)
    parser.add_argument('n', metavar='N', type=int, nargs=1)
    arguments = parser.parse_args()
    num_bits = arguments.bits[0]
    m = arguments.m[0] # q
    n = arguments.n[0] # r

    print("Encrypting using: " + str(num_bits) + " bits, Message: m: " + str(m) + " n: " + str(n))
    napsack = [0] * num_bits
    # Generate our napsack
    #napsack[0] = random.randint(1, 4) # create a random first entry
    sum = 0
    for i in range(0, num_bits):
        sum += random.randint(1, 4) + sum # create random next entry
        napsack[i] = sum
    print("Our napsack: " + str(napsack))
    # generate our message
    message = [0] * num_bits
    for i in range(0, num_bits):
        rando = random.randint(1,200)
        if rando % 2 == 0:
            message[i] = 1
        else:
            message[i] = 0
    print("Our message: " + str(message))
    # generate the beta array:
    betas = [0] * num_bits
    for i in range(0, num_bits):
        betas[i] = (n * napsack[i]) % m
    # encrypt the message
    encrypted_data = 0
    for i in range(0, num_bits):
        encrypted_data += message[i] * betas[i]
    print("Encrypted message: " + str(encrypted_data))
    r_inverse = modinv(2, n)
    print("Modinverse of " + str(n) + ": " + str(r_inverse))
    # decomposition:
    decomp = (encrypted_data * r_inverse) % m
    print("Decomposed data: " + str(decomp))
    # now generate our bits based on this value:
    decrypted_data = [0]*num_bits
    diff = decomp
    for i in xrange(num_bits-1, 0, -1):
        if napsack[i] < diff:
            decrypted_data[i] = 1
            diff -= napsack[i]
    print("Decrypted data: " + str(decrypted_data))




# Shamelessly copied from Stack Overflow - this math is hard
def egcd(a,b):
    if a==0:
        return(b,0,1)
    g,y,x=egcd(b%a,a)
    return (g, x - (b//a) * y, y)


def modinv(a, m):
    g,x,y = egcd(a, m)

    if g != 1:
        raise Exception('No modular inverse')
    return x%m

if __name__ == '__main__':
    main()
