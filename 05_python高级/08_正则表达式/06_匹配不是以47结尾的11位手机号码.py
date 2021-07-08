# 不是以4、7结尾的手机号码(11位)

import re

tels = ["13100001234", "18912344321", "10086", "18800007777"]
pattern = r"^1\d{9}[0-35-68-9]$"
for tel in tels:
    if re.match(pattern, tel) is not None:
        print(tel)