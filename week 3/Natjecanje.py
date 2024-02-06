"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://pythonguides.com/python-sort-list-of-tuples/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
def cmput(reserveTeams, damagedTeams):
    x = y = z = 10
    if len(reserveTeams) == 0:
        #print([damagedTeams])
        return len(damagedTeams)
    if reserveTeams[0]-1 in damagedTeams:
        copy = list(damagedTeams)
        copy.remove(reserveTeams[0]-1)
        x = cmput(reserveTeams[1:], copy) 
    if reserveTeams[0]+1 in damagedTeams:
        copy = list(damagedTeams)
        copy.remove(reserveTeams[0]+1)        
        y = cmput(reserveTeams[1:], copy)
    z = cmput(reserveTeams[1:], damagedTeams)
    #print([x,y,z])
    return min(x,y,z)
    
            
    
teams, numDamaged, numReserve = map(int, input().split())
damagedTeams =  input().split()
reserveTeams =  input().split()
for i in range(numDamaged):
    damagedTeams[i] = int(damagedTeams[i])
for i in range(numReserve):
    reserveTeams[i] = int(reserveTeams[i])
rm = []
for i in damagedTeams:
    if i in reserveTeams:
        rm.append(i)
        reserveTeams.remove(i)
for i in rm:
    damagedTeams.remove(i)
print(cmput(reserveTeams,damagedTeams))


    