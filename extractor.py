import os
from PyPaperBot import __main__ as bot
from refextract import extract_references_from_file

query = "Machine Learning"
default_scholar_pages = 1
dwn_dir = os.getcwd() + "/downloads"

os.makedirs(dwn_dir, exist_ok=True)

# Download Papers
# bot.start(query, default_scholar_pages, dwn_dir)

for dirpath, _, papers in (os.walk(dwn_dir)):
    for paper in papers:
        paper_path = os.path.join(dirpath, paper)
        print(paper_path)
        print(extract_references_from_file(paper_path))
