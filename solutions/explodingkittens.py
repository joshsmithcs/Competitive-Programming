"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
def getNext():
    global bombsRemaining
    global defuseRemaining
    global bombIter
    global defuseIter
    if bombsRemaining and defuseRemaining:
        nb = int(bombs[bombIter])
        nd = int(defuses[defuseIter])
        if nb < nd:
            bombIter+=1
            if bombIter == numBomb:
                bombsRemaining = False
            return nb, True
        else: 
            defuseIter+=1 
            if defuseIter == numDefuse:
                defuseRemaining = False        
            return nd, False            
    elif bombsRemaining:
        nb = int(bombs[bombIter])
        bombIter+=1
        if bombIter == numBomb:
            bombsRemaining = False
        return nb, True
    return -1, None
    
        
numPlayers, numBomb, numDefuse = map(int, input().split())
players = []
for i in range(numPlayers):
    players.append(i)
bombs = sorted(input().split(), key = lambda x: (len (x), x))
defuses = sorted(input().split(), key = lambda x: (len (x), x))
bombIter = 0
defuseIter = 0
defuseCardsInHand = [0]*numPlayers
base = 0
basePlayer = 0
bombsRemaining = defuseRemaining = True
#change approach don't iterate over every number use a split queue 
nextCard, bomb = getNext()
while (nextCard != -1):
    i = (basePlayer + nextCard - base) % numPlayers
    turn = players[i]
    if bomb:
        if defuseCardsInHand[turn] > 0:
            defuseCardsInHand[turn] -= 1
        else:
            numPlayers -= 1
            base = nextCard
            if i == 0:
                basePlayer = numPlayers - 1
            else: 
                basePlayer = i-1
            del players[i]
            if numPlayers == 1:
                print(players[0])
                break
    else:
        defuseCardsInHand[turn] = min(5, defuseCardsInHand[turn]+1)
    nextCard, bomb = getNext()
if numPlayers > 1:
    print("-1")