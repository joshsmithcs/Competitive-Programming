import pandas as pd
from autokattis import Kattis

username = input("Please enter your kattis username: ")
password = input("Please enter your kattis password: ")
kt = Kattis(username, password)
problems = kt.problems() 
df = problems.to_df()
df = df.drop(['id','fastest', 'shortest', 'total','acc'], axis=1)
f = open("kattis.txt", "w")
f.write(f'# Leetcode/Kattis\n\n')
f.write(f'### Repository to show a breadth of Leetcode/Kattis solutions\n\n')
f.write(f'### Leetcode statistics and solutions to be added soon\n\n')
f.write(f'## Kattis problems solved: {len(df.index)}\n\n')
f.write(f'|Problem Name|Difficulty|Category|\n')
f.write(f'|:---|:---|:---|\n')
for index, row in df.iterrows(): #iterrows is slow and not the best approach but is fine with small datasets
    f.write(f"|[{row['name']}]({row['link']})|{row['difficulty']}| {row['category']} |\n")
f.write(f'\n\nThanks to Russel for the [AutoKattis](https://github.com/RussellDash332/autokattis) kattis wrapper to be able to pull these stats.\n\n')
f.write(f'[Back to main profile](https://github.com/joshsmithcs)')
f.close()
