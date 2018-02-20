#!/bin/python2
# implement an RSA encryption and decryption system
# with the following args: int p1, int p2, int e
# we assume that p1 and p2 are prime - if they aren't, then this *probably*
# won't work at all

import argparse
import random


def main():
    print("WARNING: Feeding this program non-prime values will not go well! You have been warned!")
    print("NOTE: Pay attention to number of bits for each number.")
    parser = argparse.ArgumentParser(description='USAGE: q2.py int p1, int p2, int e')
    parser.add_argument('p1', metavar='p1', type=int, help="First prime value", nargs=1)
    parser.add_argument('p2', metavar='p2', type=int, help="Second prime value", nargs=1)
    parser.add_argument('e', metavar='e', type=int, help="Encryption element", nargs=1)
    arguments = parser.parse_args()
    # Declare our variables
    p = arguments.p1[0]
    q = arguments.p2[0]
    exponent = arguments.e[0]
    print("Given values: p1: " + str(p) + " p2: " + str(q) + " e: " + str(exponent))
    message = random.randint(1, 10000000) # generate our "message"
    print("Encrypting: " + str(message))
    # compute message ^ p1 % e
    encrypted_message = pow(message, p, exponent)
    print("Encrypted message: " + str(encrypted_message))
    # compute encrypted_message ^ p2 % e
    decrypted_message = pow(encrypted_message, q, exponent)
    print("Decrypted message: " + str(decrypted_message))
    if message == decrypted_message:
        print("Messages match")
    else:
        print("Messages don't match - did you enter prime numbers?")


if __name__ == '__main__':
    main()