"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://cp-algorithms.com/string/string-hashing.html

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import sys
cases = int(input())
d = dict()
d2 = dict()
l=[]
numTypos = 0
p = 31
m = 9223372036854775783
for i in range(cases):
    string = sys.stdin.readline()[:-1]
    hash_value = 0
    p_pow = 1
    for char in string:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    d[string] = hash_value
    d2[hash_value] = True
    #d[string] = True
    l.append(string)
for i in range(cases):
    string = l[i]
    typo = False
    hsh = d[string]
    hash_value = 0
    p_pow = 1    
    for char in string[1:]:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m  
    if hash_value in d2:
        typo = True
    else:
        p_pow = 1
        for i in range(len(string)-1):
            hash_value = (hash_value + (ord(string[i]) - ord(string[i+1])) * p_pow) % m
            p_pow = (p_pow * p) % m 
            if hash_value in d2:
                typo = True
    if typo:
        numTypos += 1
        print(string)
if numTypos == 0:
    print("NO TYPOS")