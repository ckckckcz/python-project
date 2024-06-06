import os
from random import randint

for i in range(1, 365):
    for j in range(0, randint(1, 10)):
        d = str(i) + ' beberapa hari yang lalu'
        with open('file.txt', 'a') as file:
            file.rite(d)
        os.system('git add .')
        os.system('git commit --date="' + d +'" -m "commit"')
os.system('git push -u origin main')