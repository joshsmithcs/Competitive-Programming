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
#Calculate from both the input and the solution to drastically reduce runtime
def findAllMoves(p):
    m = []
    m.append(p[1] + p[2] + p[3] + p[0] + p[4:])
    m.append(p[:4] + p[5] + p[6] + p[7] + p[4] + p[8:])
    m.append(p[:8] + p[9] + p[10] + p[11] + p[8] + p[12:])
    m.append(p[:12] + p[13] + p[14] + p[15] + p[12])
    
    m.append(p[3] + p[0] + p[1] + p[2] + p[4:])
    m.append(p[:4] + p[7] + p[4] + p[5] + p[6] + p[8:])
    m.append(p[:8] + p[11] + p[8] + p[9] + p[10] + p[12:])
    m.append(p[:12] + p[15] + p[12] + p[13] + p[14])
    
    m.append(p[4] + p[1:4] + p[8] + p[5:8] + p[12] + p[9:12] + p[0] + p[13:])
    m.append(p[0] + p[5] +  p[2:5] + p[9] + p[6:9] + p[13] + p[10:13] + p[0] + p[14:]) 
    m.append(p[0:2] + p[6] +  p[3:6] + p[10] + p[7:10] + p[14] + p[11:14] + p[2] + p[15])
    m.append(p[0:3] + p[7] +  p[4:7] + p[11] + p[8:11] + p[15] + p[12:15] + p[3])
    
    m.append(p[12] + p[1:4] + p[0] + p[5:8] + p[4] + p[9:12] + p[8] + p[13:])
    m.append(p[0] + p[13] +  p[2:5] + p[1] + p[6:9] + p[5] + p[10:13] + p[9] + p[14:])  
    m.append(p[0:2] + p[14] +  p[3:6] + p[2] + p[7:10] + p[6] + p[11:14] + p[10] + p[15])
    m.append(p[0:3] + p[15] +  p[4:7] + p[3] + p[8:11] + p[7] + p[12:15] + p[11])
    

    return m
             
cube = ""
ans = "RRRRGGGGBBBBYYYY"
for i in range(4):
    cube = cube + input()
d = dict()
d[cube] = 0
d[ans] = 100
newPositions = [cube]
move = 1
found = False
foundMove = 0
if cube == ans:
    print("0")
else:
    while(move < 7):
        positions = newPositions
        newPositions = []
        for p in positions:
            x = findAllMoves(p)
            for m in x:
                if m in d:
                    if d[m] > 10:
                        found = True
                        foundMove = move
                        break
                else:
                    d[m] = move
                    newPositions.append(m)
            if found:
                break
        if found:
            break
        move += 1
    if found:
        print(foundMove)
    else:
        #go backwards
        move = 1
        newPositions = [ans]
        while(move < 7):
            positions = newPositions
            newPositions = []
            for p in positions:
                x = findAllMoves(p)
                for m in x:
                    if m in d:
                        if d[m] > 10:
                            found = True
                            foundMove = move
                            break
                    else:
                        d[m] = move
                        newPositions.append(m)
                if found:
                    break
            if found:
                break
            move += 1    
        print(foundMove+6)
        
    
