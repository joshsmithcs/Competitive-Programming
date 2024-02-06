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
"""
cards = int(input()) 
Anthony = [int(x) for x in input().split()]
Matthew = [int(x) for x in input().split()]
pointsAnthony = 0
pointsMatthew = 0
pointerAnthony = 0
pointerMatthew = 0
turn = 0
d = dict()
d2 = dict()
pairsFound = 0
while(pairsFound < cards):
    if turn == 0:
        while(Anthony[pointerAnthony] in d):
            pointerAnthony += 1
        card1 = Anthony[pointerAnthony]
        pointerAnthony += 1
        d[card1] = True
        if card1 // 2 in d2:
            pointsAnthony += 1
            pairsFound += 1            
        else:
            while(Anthony[pointerAnthony] in d):
                pointerAnthony += 1
            card2 = Anthony[pointerAnthony]
            pointerAnthony += 1
            d[card2] = True        
            if card1 // 2 == card2 // 2:
                pointsAnthony += 1
                pairsFound += 1
            else:
                if card1//2 in d2:
                    pointsMatthew += 1
                    pairsFound += 1
                else:
                    d2[card1//2] = True
                if card2//2 in d2:
                    pointsMatthew += 1
                    pairsFound += 1
                else:
                    d2[card2//2] = True
                turn = 1
    else:
        while(Matthew[pointerMatthew] in d):
            pointerMatthew += 1
        card1 = Matthew[pointerMatthew]
        pointerMatthew += 1
        d[card1] = True
        if card1 // 2 in d2:
            pointsMatthew += 1
            pairsFound += 1  
        else:
            while(Matthew[pointerMatthew] in d):
                pointerMatthew += 1
            card2 = Matthew[pointerMatthew]
            pointerMatthew += 1
            d[card2] = True        
            if card1 // 2 == card2 // 2:
                pointsMatthew += 1
                pairsFound += 1
            else:
                if card1//2 in d2:
                    pointsAnthony += 1
                    pairsFound += 1
                else:
                    d2[card1//2] = True
                if card2//2 in d2:
                    pointsAnthony += 1
                    pairsFound += 1
                else:
                    d2[card2//2] = True
                turn = 0
if pointsAnthony > pointsMatthew:
    print("0")
elif pointsMatthew > pointsAnthony:
    print("1")
else:
    print("-1")
            
            
        
    

