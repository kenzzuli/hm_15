# 需求：匹配出0-100之间的数字
# 0 1 11 100 都有效
# 08 010无效

import re

pattern = r"^([1-9]?\d|100)$"
nums = ["0", "8", "78", "08", "100", "1000", "010"]
for num in nums:
    res = re.match(pattern, num)
    if res is None:
        pass
    else:
        print(num)
