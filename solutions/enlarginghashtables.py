"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925890/mod_resource/content/4/403_numtheory_2022.pdf

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import math
primes = []
mx = 2 ** 16
arr = [1] * (mx+2)
for i in range(2, mx+2):
    if arr[i]:
        primes.append(i)
    for j in range(i*2, mx+2, i):
        arr[j] = 0
n = int(input())
while(n > 0):
    nNotPrime = False
    sqrtN = int(math.sqrt(n))
    p = 2
    while(p <= sqrtN):
        if n%p == 0:
            nNotPrime = True
            break
        p +=1
    m = 2 * n + 1
    found = 0
    while(found == 0):
        sqrtM = int(math.sqrt(m))
        prime = True
        p = 3
        itr = 1
        while(p <= sqrtM):
            if m%p == 0:
                prime = False
                break
            itr += 1
            p += primes[itr]
        if prime:
            found = m
        m += 2
    if nNotPrime:
        print(str(found) + " (" + str(n) + " is not prime)")
    else:
        print(found)
    n = int(input())
