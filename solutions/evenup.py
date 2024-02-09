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
import math 

def evenup(numbers, count):
    if count > 50:
        shalf = count // 2
        bhalf = math.ceil(count / 2)
        
        a, c = evenup(numbers[:shalf], shalf) 
        b, d = evenup(numbers[shalf:], bhalf)
        while(c>0 and d>0 and a[c-1] == b[0]):
            a = a[:-1]
            c -= 1
            b = b[1:]
            d -= 1
        return a+b, c+d
    else:
        changed = True
        while(changed):
            changed = False
            i=0
            while(i < count - 1):
                if( numbers[i] == numbers[i+1]):
                    del numbers[i:i+2]
                    changed = True
                    count -= 2
                    if i > 0:
                        i -= 1
                else:
                    i+=1
        return numbers, count
    
count = int(input())
numbers = input().split()
changed = True

for i in range(count):
    numbers[i] = int(numbers[i]) % 2

numbers, count = evenup(numbers, count)
                 
print(count)