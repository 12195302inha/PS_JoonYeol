import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    factors = list(map(int, sys.stdin.readline().split()))
    factors.sort()
    print(factors[0] * factors[-1])
