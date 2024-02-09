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
from sys import stdin
ram = [0]*1000
registers = [0]*10
i = 0
for line in stdin:
    ram[i] = int(line)
    i += 1
halt=False
location=0
steps = 0
while(not(halt)):
    steps += 1
    instruct = ram[location] // 100
    x = ram[location] // 10 % 10
    y = ram[location] % 10
    if instruct > 4:
        if instruct > 7:
            if instruct == 8:
                registers[x] = ram[registers[y]]
                location += 1 
            else:
                ram[registers[y]] = registers[x]
                location += 1
        else:
            if instruct == 5:
                registers[x] = registers[y]
                location += 1 
            elif instruct == 6:
                registers[x] = (registers[x] + registers[y]) % 1000
                location += 1                 
            else:
                registers[x] = (registers[x] * registers[y]) % 1000
                location += 1                                   
    else:
        if instruct > 2:
            if instruct == 3:
                registers[x] = (registers[x] + y) % 1000
                location += 1                  
            else:
                registers[x] = (registers[x] * y) % 1000
                location += 1                   
                
        else:
            if instruct == 0:
                if registers[y] != 0:
                    location = registers[x]
                else:
                    location += 1 
            elif instruct == 1: 
                halt = True
            else:
                registers[x] = y
                location += 1    
print(steps)