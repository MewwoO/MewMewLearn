"""
ddd
"""

# coding=utf-8
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

word = "disabled"
print(f"https://www.youdao.com/result?word={word}&lang=en")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}
request = urllib.request.Request(
    "https://www.youdao.com/result?word={word}&lang=en", headers=headers
)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

# 解析
soup = BeautifulSoup(content, "html.parser")
divs = soup.find_all("div", {"class": "per-phone"})

data_us = []
data_uk = []
for k, div in enumerate(divs):
    phonetic_spans = div.find_all("span", {"class": "phonetic"})
    for span in phonetic_spans:
        if k == 0:
            data_us.append({"英式音标": span.text})
        if k == 1:
            data_uk.append({"美式音标": span.text})

df_us = pd.DataFrame(data_us)
df_uk = pd.DataFrame(data_uk)
df = pd.concat([df_us, df_uk], axis=1)
print(df)
