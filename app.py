import os
from random import randint, sample
from datetime import datetime, timedelta

# Total days in a year (non-leap year)
total_days = 365

# List of months and corresponding number of days
months = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 'December': 31
}

# Ensure every Monday, Wednesday, and Friday of each month has at least one commit
for month, days_in_month in months.items():
    for day in range(1, days_in_month + 1):
        current_date = datetime.strptime(month[:3] + ' ' + str(day), '%b %d')
        if current_date.weekday() in [0, 2, 4]:  # Monday, Wednesday, Friday
            d = current_date.strftime('%d beberapa hari yang lalu')
            with open('file.txt', 'a') as file:
                file.write(d + '\n')
            os.system('git add .')
            os.system('git commit --date="' + d +'" -m "commit"')

# Add extra commits to random days to spread out contributions
extra_commits = 1000  # total number of additional commits
if extra_commits > total_days:
    extra_commits = total_days  # Avoid sampling more than the total number of days

days_with_extra_commits = sample(range(1, total_days + 50), extra_commits)

for day in days_with_extra_commits:
    current_date = datetime.strptime('Jan 1', '%b %d') + timedelta(days=day - 1)
    if current_date.weekday() in [0, 2, 4]:  # Monday, Wednesday, Friday
        d = current_date.strftime('%d beberapa hari yang lalu')
        with open('file.txt', 'a') as file:
            file.write(d + '\n')
        os.system('git add .')
        os.system('git commit --date="' + d +'" -m "extra commit"')

os.system('git push -u origin main')
