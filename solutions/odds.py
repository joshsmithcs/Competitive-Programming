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
def gcd(a,b):
    if b:
        return gcd(b, a%b)
    return a

odds = {
    21 : 34,
    12 : 34,
    66 : 33,
    55 : 32,
    44 : 31,
    33 : 30,
    22 : 29,
    11 : 28,
    65 : 26,
    56 : 26,
    64 : 24,
    46 : 24,
    63 : 22,
    36 : 22,
    62 : 20,
    26 : 20,
    61 : 18,
    16 : 18,
    54 : 16,
    45 : 16,
    53 : 14,
    35 : 14,
    52 : 12,
    25 : 12,
    51 : 10,
    15 : 10,
    43 : 8,
    34 : 8,
    42 : 6,
    24 : 6,
    41 : 4,
    14 : 4,
    32 : 2,
    23 : 2,
    31 : 0,
    13 : 0
}
while(True):
    my1, my2, enemy1, enemy2 = input().split()
    if my1 == "0":
        break
    #if my1 == "*" and my2 == "*" and enemy1 == "*" and enemy2 == "*":
        #print("205/432")
        #continue
    myScores = []
    if my1 == "*" and my2 == "*":
        for i in odds.values():
            myScores.append(i)
    elif my1 == "*":
        for i in range(1,7):
            s = [int(my2), i]
            myScores.append(odds[s[0]*10+s[1]])
    elif my2 == "*":
        for i in range(1,7):
            s = [int(my1), i]
            myScores.append(odds[s[0]*10+s[1]])
    else:
        s = [int(my1), int(my2)]
        myScores.append(odds[s[0]*10+s[1]])
    enemyScores = []
    if enemy1 == "*" and enemy2 == "*":
        for i in odds.values():
            enemyScores.append(i)
    elif enemy1 == "*":
        for i in range(1,7):
            s = [int(enemy2), i]
            s.sort(reverse=True)
            enemyScores.append(odds[s[0]*10+s[1]])
    elif enemy2 == "*":
        for i in range(1,7):
            s = [int(enemy1), i]
            s.sort(reverse=True)
            enemyScores.append(odds[s[0]*10+s[1]])
    else:
        s = [int(enemy1), int(enemy2)]
        s.sort(reverse=True)
        enemyScores.append(odds[s[0]*10+s[1]])    
    attempts = 0
    wins = 0
    for i in range(len(myScores)):
        for j in range(len(enemyScores)):
            attempts += 1
            if myScores[i] > enemyScores[j]:
                wins += 1
    if wins == attempts:
        print("1")
    elif wins == 0:
        print(0)
    else:
        g = gcd(wins, attempts)
        print(str(wins//g) + "/" + str(attempts//g))
    
        