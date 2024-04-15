"""
sss
"""

import pandas as pd

# 读取表格数据
df = pd.read_excel(r"Day 01\1_phrase.xlsx")

# 选择需要的列并重命名列名
df = df[["单词", "释义"]]
df.columns = ["词组", "词组含义"]

# 去除空行
df = df.dropna()

# 保存为新的 Excel 文件
df.to_excel(r"Day 01\1_phrase.xlsx", index=False, header=None)
