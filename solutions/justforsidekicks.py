"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://www.geeksforgeeks.org/sqrt-square-root-decomposition-technique-set-1-introduction/  This code is contributed by Sanjit_Prasad
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/FenwickTree.py
  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
# Python 3 program to demonstrate working of Square Root
# Decomposition.
from math import sqrt
from sys import stdin, stdout

MAXN = 200000
SQRSIZE = 600

arr = [0]*(MAXN)         # original array
block = []     # decomposed array
for i in range(SQRSIZE):
    block.append([0,0,0,0,0,0])
blk_sz = 0                 # block size

# Time Complexity : O(1)
def update(idx, val):
    blockNumber = idx // blk_sz
    block[blockNumber][val-1] += 1
    block[blockNumber][arr[idx]-1] -= 1
    arr[idx] = val

# Time Complexity : O(sqrt(n))
def query(l, r):
    count = [0,0,0,0,0,0]
    while (l < r and l % blk_sz != 0 and l != 0):
        # traversing first block in range
        count[arr[l]-1] += 1
        l += 1

    while (l + blk_sz <= r):
        # traversing completely overlapped blocks in range
        
        count[0] += block[l//blk_sz][0]
        count[1] += block[l//blk_sz][1]
        count[2] += block[l//blk_sz][2]
        count[3] += block[l//blk_sz][3]
        count[4] += block[l//blk_sz][4]
        count[5] += block[l//blk_sz][5]
        l += blk_sz

    while (l <= r):
        # traversing last block in range
        count[arr[l]-1] += 1
        l += 1

    sm = 0
    for i in range(6):
        sm += count[i] * values[i]
    return sm

# Fills values in input[]
def preprocess(input, n):

    # initiating block pointer
    blk_idx = -1

    # calculating size of block
    global blk_sz
    blk_sz = int(sqrt(n))
    # building the decomposed array
    for i in range(n):
        arr[i] = int(input[i]);
        if (i % blk_sz == 0):

            # entering next block
            # incrementing block pointer
            blk_idx += 1;

        block[blk_idx][arr[i]-1] += 1



N, Q = map(int, input().split())
values = []
v = input().split()
for i in range(6):
    values.append(int(v[i]))
data = input()
preprocess(data, N)

for i in range(Q):
    o, I1, I2 = map(int, stdin.readline().split())
    if o == 1:
        update(I1-1, I2)
    elif o == 2:
        values[I1 - 1] = I2
    else:
        stdout.write('{}\n'.format(query(I1-1, I2-1)))
        
        