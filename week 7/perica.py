"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://eclass.srv.ualberta.ca/pluginfile.php/7925890/mod_resource/content/4/403_numtheory_2022.pdf
  https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import math 
modulo = 1000000007
def modInverse(num):
    if num in d2:
        return d2[num]
    else:
        a = num
        m = modulo
        m0 = m
        y = 0
        x = 1
     
        while (a > 1):
     
            # q is quotient
            q = a // m
     
            t = m
     
            # m is remainder now, process
            # same as Euclid's algo
            m = a % m
            a = t
            t = y
     
            # Update x and y
            y = x - q * y
            x = t
     
        # Make x positive
        if (x < 0):
            x = x + m0
        d2[num] = x
        return x

d = dict()
d[0] = 1
fact = 1
d2 = dict()
for i in range(1, 100001):
    fact = fact * i % modulo
    d[i] = fact 
N, K = map(int, input().split())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
a.sort(reverse=True)
ans = 0
for i in a:
    if N >= K:
        ans += i * d[N-1] * modInverse(d[K-1]) * modInverse(d[N-K]) 
        ans = ans %modulo
        N -= 1
print(int(ans))