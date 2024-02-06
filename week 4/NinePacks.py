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

hotdogs = input().split()
bunpacks = input().split()
countDog = int(hotdogs[0])
countBun = int(bunpacks[0])
if (countBun and countDog):
    dog = dict()
    dog[0] = 0
    for i in range(countDog):
        num = int(hotdogs[i+1])
        s = dog.copy()  
        for j in s:
            if j + num in dog:
                dog[j+num] = min(dog[j+num], s[j]+1)
            else:
                dog[j+num] = s[j]+1
    del dog[0]
    bun = dict()
    bun[0] = 0
    for i in range(countBun):
        num = int(bunpacks[i+1])
        s = bun.copy()
        for j in s:
            if j + num in bun:
                bun[j+num] = min(bun[j+num], s[j]+1)
            else:
                bun[j+num] = s[j]+1
    del bun[0]
    match = 201
    dogIter = 0
    dogCombos = sorted(list(dog.keys()))
    curDog = dogCombos[0]
    bunIter = 0
    bunCombos = sorted(list(bun.keys()))
    curBun = bunCombos[0]
    while(True):
        if curDog > curBun:
            bunIter += 1
            if bunIter == len(bunCombos):
                break
            curBun = bunCombos[bunIter]
        elif curDog < curBun: 
            dogIter += 1
            if dogIter == len(dogCombos):
                break
            curDog = dogCombos[dogIter]   
        else:
            match = min(match, dog[curDog] + bun[curBun])
            bunIter += 1
            if bunIter == len(bunCombos):
                break
            curBun = bunCombos[bunIter] 
            dogIter += 1
            if dogIter == len(dogCombos):
                break
            curDog = dogCombos[dogIter]              
    if match == 201:
        print("impossible")
    else: 
        print(match)
    
else:
    print("impossible")