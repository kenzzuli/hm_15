import re
from parse_url import parse_url
import json
from pprint import pprint

url = "https://36kr.com/"
html_str = parse_url(url)
pattern = r"<script>window.initialState=(.*?)</script>"
ret = re.findall(pattern, html_str)
# 写入本地文件，查找规律
# for i in ret:
#     tmp = json.loads(i)
#     with open("36kr.json", mode="w", encoding="utf8") as f:
#         json.dump(tmp, f, ensure_ascii=False, indent=2)
#     pprint(tmp)

# 提取目标字段
for i in ret:
    tmp = json.loads(i)
    item_list = tmp["homeData"]["data"]["homeFlow"]["data"]["itemList"]
    for item in item_list:
        try:
            item = item["templateMaterial"]
            print(item["widgetTitle"])
            print(item["summary"])
            print(item["authorName"])
            print("*" * 50)
        except:
            continue
