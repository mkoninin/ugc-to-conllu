# %%

# тут я хочу выделить общие слова в чатах, чтобы потом их исключать

import conllu
import matplotlib.pyplot as plt
import pandas as pd
import json, itertools, os
import datetime
from collections import Counter

from tganalysis import tganalysis

paths = ['C:/Users/mk/Downloads/Telegram Desktop/ChatExport_2023-12-20']

# paths = os.listdir('data')

paths
# %%
words = {}

for path in paths:
    filename = os.path.join('data', path, 'result.json')

    tg = tganalysis.tg_json_analysis(filename)


# %%
ids = list(tg.ids)
for id in ids:
    try:
        text = tg.df[id].text
        open('tg.conllu', 'a').write(conllu.conllu(text))

# %%
tg.df[list(tg.ids)[9]]
# %%
