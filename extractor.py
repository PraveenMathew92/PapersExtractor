import os
from PyPaperBot import __main__ as bot
import json
import pandas
from crossref.restful import Works

import rpy2
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector
from rpy2.robjects.packages import importr
utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)

# Install packages
packnames = ('rcrossref')
utils.install_packages(StrVector(packnames))

# Load packages
rcrossref = importr('rcrossref')

query = "Machine Learning"
default_scholar_pages = 1
dwn_dir = os.getcwd() + "/downloads/"

os.makedirs(dwn_dir, exist_ok=True)

# Download Papers
# bot.start(query, default_scholar_pages, dwn_dir)

works = Works()
results_csv = pandas.read_csv('result.csv')
dois = results_csv['DOI']

for doi in dois:
    details = works.doi(doi)
    print(json.dumps(details))
    print(rcrossref.cr_abstract(doi))

# for dirpath, _, papers in (os.walk(dwn_dir)):
#     for paper in papers:
#         paper_path = os.path.join(dirpath, paper)
#         print(paper_path)
        # print(extract_references_from_file(paper_path))
