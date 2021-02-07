import os
from PyPaperBot import __main__ as bot
from inspect import getmembers, isfunction

query = "Machine Learning"
default_scholar_pages = 1
dwn_dir = os.getcwd()


print(bot.start(query, default_scholar_pages, dwn_dir))

# print(start(query, default_scholar_pages, dwn_dir))