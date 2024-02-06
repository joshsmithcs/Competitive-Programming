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

word = dict()
number = dict()
for line in stdin:
    line = line.split()
    if line[0] == "clear":
        word.clear()
        number.clear()
    else:
        if line[0] == "def":
            if line[1] in word:
                number.pop(word[line[1]])
            word[line[1]] = line[2]
            number[line[2]] = line[1]
        else:
            l = len(line)
            line = line[1:l]
            steps = l//2 
            valid = True
            for i in range(steps):
                if not(line[i*2] in word):
                    valid = False
                    line = " ".join(line)
                    print(line + " unknown")                    
                    break
                ans = int(word[line[0]])
            if valid:
                steps -=  1
                for i in range(steps):
                    if line[i*2+1] == "+":
                        ans = ans + int(word[line[i*2+2]])
                    else:
                        ans = ans - int(word[line[i*2+2]])
                if str(ans) in number:
                    ans = number[str(ans)]
                else:
                    ans = "unknown"
                line = " ".join(line)
                print(line + " " + ans)

        