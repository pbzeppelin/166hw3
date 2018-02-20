#!/bin/python2
# something something GPL v3
# Q1: 4 points max: Implement a fully functional knapsack crypto system:
# knapsack( int bits, int m, int n) should create a knapsack system for
# the given number of bits and the given values of m and n.
# (The example given in textbook has 8 bits).
#   Use your code to encode and decode a message and prove that it works.
# If you are not coding, your example knapsack should be at least 12 bits.

import argparse

def main():
    parser = argparse.ArgumentParser(description='USAGE: q1.py int bits, int m, int n')
    parser.add_argument('bits', metavar='bits', type=int, nargs=1)
    parser.add_argument('m', metavar='M', type=int, nargs=1)
    parser.add_argument('n', metavar='N', type=int, nargs=1)
    arguments = parser.parse_args()
    num_bits = arguments.bits[0]
    m = arguments.m[0]
    n = arguments.n[0]
    print("Encrypting using: " + str(num_bits) + " bits, m: " + str(m) + " n: " + str(n))


if __name__ == '__main__':
    main()
