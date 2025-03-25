import pandas as pd
import json

# 读取 JSON 文件
with open("investor.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 转换为 DataFrame
df = pd.DataFrame(data)

# 保存为 CSV 文件
df.to_csv("investors.csv", index=False)
print("✅ 成功保存为 investors.csv")
