import os
from PyPaperBot import __main__ as bot
from inspect import getmembers, isfunction

query = "Machine Learning"
default_scholar_pages = 1
dwn_dir = os.getcwd() + "/downloads"

os.makedirs(dwn_dir, exist_ok=True)

# Download Papers
# bot.start(query, default_scholar_pages, dwn_dir)

for _, _, papers in (os.walk(dwn_dir)):
    for paper in papers:
        print(paper)
