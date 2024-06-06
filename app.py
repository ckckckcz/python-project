import os
from random import randint, sample

# Total days in a year (non-leap year)
total_days = 365

# Ensure every day has at least one commit
for i in range(1, total_days + 1):
    d = str(i) + ' beberapa hari yang lalu'
    with open('file.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add .')
    os.system('git commit --date="' + d +'" -m "commit"')

# Add extra commits to random days to spread out contributions
extra_commits = 1000  # total number of additional commits
if extra_commits > total_days:
    extra_commits = total_days  # Avoid sampling more than the total number of days

days_with_extra_commits = sample(range(1, total_days + 1), extra_commits)


for day in days_with_extra_commits:
    d = str(day) + ' beberapa hari yang lalu'
    with open('file.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add .')
    os.system('git commit --date="' + d +'" -m "extra commit"')

os.system('git push -u origin main')
