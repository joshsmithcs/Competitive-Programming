import pandas as pd
from autokattis import Kattis
import requests


kattisUsername = "joshua-smith5"
leetcodeUsername = "user5583Dn"
githubLink = "https://github.com/joshsmithcs/Competitive-Programming/blob/main/solutions/"

kattisPassword = input("Please enter your kattis password: ")

#create file and headers
f = open("kattis.txt", "w")
f.write(f'# Competitive Programming\n\n')
f.write(f'### Repository to show a breadth of Leetcode/Kattis stats\n\n')

#get leetcode stats
leetcodeStatsApi = "https://leetcode-stats-api.herokuapp.com/" + leetcodeUsername
leetcodeStats = requests.get(leetcodeStatsApi).json()

#write leetcode stats
f.write(f'## [Leetcode Profile](https://leetcode.com/{leetcodeUsername}/)\n\n')
f.write(f'## Leetcode problems solved: {leetcodeStats["totalSolved"]}\n\n')
f.write(f'|Easy|Medium|Hard|\n')
f.write(f'|:---|:---|:---|\n')
f.write(f'|{leetcodeStats["easySolved"]}|{leetcodeStats["mediumSolved"]}|{leetcodeStats["hardSolved"]}|\n')

#get kattis stats and problem list
kt = Kattis(kattisUsername, kattisPassword)
problems = kt.problems() 
data = problems.to_df()
data = data.drop(['fastest', 'shortest', 'total','acc'], axis=1)
kattisEasy = data['category'].value_counts()['Easy']
kattisMedium = data['category'].value_counts()['Medium']
kattisHard = data['category'].value_counts()['Hard']


#write kattis stats
f.write(f'\n\n## [Kattis Profile](https://open.kattis.com/users/{kattisUsername})\n\n')
f.write(f'## Kattis problems solved: {len(data.index)}\n\n')
f.write(f'|Easy|Medium|Hard|\n')
f.write(f'|:---|:---|:---|\n')
f.write(f'|{kattisEasy}|{kattisMedium}|{kattisHard}|\n')
f.write(f'\nLinks currently only working for python solutions, if 404 look in solutions folder!\n\n')
f.write(f'|Problem|Difficulty|Category|Link|\n')
f.write(f'|:---|:---|:---|:---|\n')
for index, row in data.iterrows(): #iterrows is slow and not the best approach but is fine with small datasets
    # most solutions are in python, this will not work for other languages currently
    f.write(f"|[{row['name']}]({row['link']})|{row['difficulty']}| {row['category']} |[solution]({githubLink}{row['id']}.py)|\n")


#write recognitions
f.write(f'\n\nThanks to Jeremy for the [LeetCodeStatsApi](https://github.com/JeremyTsaii/leetcode-stats-api) Api to be able to fetch leetcode solve stats.\n\n')
f.write(f'Thanks to Russel for the [AutoKattis](https://github.com/RussellDash332/autokattis) kattis wrapper to be able to pull kattis stats and problem links.\n\n')
f.write(f'[Back to main profile](https://github.com/joshsmithcs)')
f.close()
