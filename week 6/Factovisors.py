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
import sys
line = sys.stdin.readline()
while True:        
    if line == "":
        break
    B, A = map(int, line.split())
    #edge cases
    if A == 1:
        print(str(A) + " divides " + str(B) + "!")
    elif A == 0 or B < 2:
        print(str(A) + " does not divide " + str(B) + "!")
    else:
        #print(A, B)
        p = 2
        primes = dict()
        a = A
        while(p*p <= a):
            if a%p == 0:
                primes[p] = 1
                a = a//p
                while ( a%p == 0 ):
                    primes[p] += 1
                    a = a//p
            p+=1
        if a>1:
            primes[a] = 1
        primeItems = primes.items()
        #print(primeItems)
        success = True
        for pair in primeItems:
            (num, count) = pair
            bItr = 1
            while(bItr < B):
                bItr = bItr * num
                lItr = bItr
                while(count > 0 and lItr <= B):
                    count -= 1 
                    lItr += bItr
            if count > 0:
                success = False
        if success:
            print(str(A) + " divides " + str(B) + "!")
        else:
            print(str(A) + " does not divide " + str(B) + "!")
    line = sys.stdin.readline()