#!/usr/bin/env python3
import argparse
from sys import exit
from sympy import *
from  Cryptodome.Util.number import bytes_to_long

def main(e, N, c):
    p = 0
    q = 0
    
    start = N // 2
    for i in range(start, start + 100000):
        if N % i == 0:
            p = i
            break
    if p == 0:
        print("Failed to factor N")
        exit(1)
    q = N // p
    print("p is prime:", isprime(p))
    print("q is prime:", isprime(q))
    
    phi = (p - 1) * (q - 1)
    try:
        d = pow(e, -1, phi)
    except ValueError:
        print("e is not invertible modulo phi")
        exit(1)
    
    m = pow(c, d, N)  # Note: exponent is d, modulus is N (not d!)
    flag = flag = m.to_bytes((m.bit_length()-7)//8 + 1, 'big')
    print(f'this is the flag : {flag}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", required=True, type=int, help="e of the RSA encryption")
    parser.add_argument("-N", required=True, type=int, help="N of the RSA encryption")
    parser.add_argument("-c", "--cypher_text", required=True, type=int, help="the ciphertext")
    args = parser.parse_args()
    main(args.e, args.N, args.cypher_text)