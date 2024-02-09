import sys

for line in sys.stdin:
    n,m = map(int, line.split())
    print(abs(n-m))