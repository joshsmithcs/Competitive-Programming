"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>

  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
  
  
  test case 
41 37
5
11 18
31 34
26 33
23 31
21 27

expected
662474291

mine
662468988
662468781

"""
import math
modulo = 1000000007
def amount(one, two):
    w1, h1 = one
    w2, h2 = two
    return (math.factorial(w2-w1+h2-h1)/ (math.factorial(w2-w1) * math.factorial(h2-h1))) % modulo

def calc(*args):
    total = 1
    for n in args:
        total = ((total) * (n)) %modulo
    return total
#calculate paths by multiplying number that can reach cheese and number that can go from there then get rid of duplicates
w, h = map(int, input().split())
numCheese = int(input())
cheese = []
for i in range(numCheese):
    c1, c2 = map(int, input().split())
    cheese.append((c1, c2))
cheese = sorted(cheese)
#print(cheese)
tot = 0
d = dict()
for c in range(len(cheese)):
    d[c] = amount(cheese[c], (w,h))
    plus = calc(amount((1,1), cheese[c]) * d[c])
    print(calc(amount((1,1), cheese[c]) * d[c]), c)
    for c2 in range(c):
        if cheese[c2][1] <= cheese[c][1]:
            d[(c2, c)] =  amount(cheese[c2], cheese[c])
            plus -= calc(amount((1,1), cheese[c2]) * d[(c2, c)] * d[c])
            print(-calc(amount((1,1), cheese[c2]) * d[(c2, c)] * d[c]) , c, c2)
            for c3 in range(c2):
                if cheese[c3][1] <= cheese[c2][1]:
                    d[(c3, c2)] = amount(cheese[c3], cheese[c2])
                    plus += calc(amount((1,1), cheese[c3]) * d[(c3, c2)] * d[(c2, c)] * d[c])
                    print(calc(amount((1,1), cheese[c3]) * d[(c3, c2)] * d[(c2, c)] * d[c]), c, c2, c3)
                    for c4 in range(c3):
                        if cheese[c4][1] <= cheese[c3][1]:
                            d[(c4, c3)] = amount(cheese[c4], cheese[c3])
                            plus -= calc(amount((1,1), cheese[c4]) * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c]) 
                            print(-calc(amount((1,1), cheese[c4]) * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c]), c, c2, c3, c4)
                            for c5 in range(c4):
                                if cheese[c5][1] <= cheese[c4][1]:                            
                                    d[(c5, c4)] = amount(cheese[c5], cheese[c4])
                                    plus += calc(amount((1,1), cheese[c5])* d[(c5, c4)] * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c])
                                    print(calc(amount((1,1), cheese[c5])* d[(c5, c4)] * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c]), c, c2, c3, c4, c5)
                                    for c6 in range(c5):
                                        print("wtf")
                                        if cheese[c6][1] <= cheese[c5][1]:                            
                                            d[(c6, c5)] = amount(cheese[c6], cheese[c5])
                                            plus -= amount((1,1), cheese[c6])* d[(c6, c5)] * d[(c5, c4)] * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c]
                                            for c7 in range(c6):
                                                if cheese[c7][1] <= cheese[c6][1]:                            
                                                    d[(c7, c6)] = amount(cheese[c7], cheese[c6])
                                                    plus += amount((1,1), cheese[c7]) * d[(c7, c6)] * d[(c6, c5)] * d[(c5, c4)] * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c]   
                                                    for c8 in range(c7):
                                                        if cheese[c8][1] <= cheese[c7][1]:                            
                                                            d[(c8, c7)] = amount(cheese[c8], cheese[c7])
                                                            plus -= amount((1,1), cheese[c8]) * d[(c8, c7)] * d[(c7, c6)] * d[(c6, c5)] * d[(c5, c4)] * d[(c4, c3)] * d[(c3, c2)] * d[(c2, c)] * d[c]                                                       
                                    
    tot += plus
    
print(int(tot % modulo))