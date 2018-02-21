#!/bin/python2
import sys
import fractions
import argparse
import random
def main():
    print("Generating coprime for: " + sys.argv[1])
    looping = True
    parser = argparse.ArgumentParser(description='USAGE: coprimes.py int value')
    parser.add_argument('value', metavar='value', type=int, nargs=1)
    arguments = parser.parse_args()
    value = arguments.value[0]
    for i in range(random.randint(2,value-1),value):
        if fractions.gcd(i, value) is 1:
            print(str(i))
            break

if __name__ == '__main__':
        main()
