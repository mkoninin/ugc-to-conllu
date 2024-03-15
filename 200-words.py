# %%

# тут я хочу выделить общие слова в чатах, чтобы потом их исключать

import matplotlib.pyplot as plt
import pandas as pd
import json, itertools, os
import datetime
from collections import Counter

import tganalysis

paths = ['C:/Users/mk/Downloads/Telegram Desktop/ChatExport_2023-12-20']

# paths = os.listdir('data')

paths
# %%
words = {}

for path in paths:
    filename = os.path.join('data', path, 'result.json')

    tg = tganalysis.tg_json_analysis(filename)

    output_path = f'output/tg-{tg.chat_id}'
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    tg._genWords()
    words[tg.chat_id] = tg.lexicon.most_common(500)

# %%
tg.df[list(tg.ids)[0]].text
