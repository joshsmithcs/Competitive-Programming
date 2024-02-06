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
#has to be much faster, maybe there is a way to estimate based off of density but not sure
wImage, hImage = map(int, input().split())
image = []
for i in range(hImage):
    pixels = input().split()
    image.append(pixels)
wUni, hUni = map(int, input().split())
uni = []
for i in range(hUni):
    pixels = input().split()
    uni.append(pixels)
wIterations = wUni - wImage + 1
hIterations = hUni - hImage + 1
closest = 0
combos = []
for startingY in range(hIterations):
    for startingX in range(wIterations):
        score = 0
        for i in range(hImage):
            for j in range(wImage):
                if image[i][j] == uni[startingY+i][startingX+j]:
                    score += 1
        if score > closest:
            combos = [(startingX, startingY)]
            closest = score
        elif score == closest:
            combos.append((startingX, startingY))
for i in combos:
    print(str(i[0]) + " " + str(i[1]))
            
            