import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dig", help="Digit to convert")
args = parser.parse_args()

try:
    digit = int(args.dig)
    if digit < 0:
        raise ValueError
    print(f"This is the number {args.dig} in binary: {bin(digit)[2:]}")
except ValueError:
    print("Usage: python3 script_name.py <non-negative-integer>")