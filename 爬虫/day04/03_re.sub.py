import re

a = "hello2world3"
print(re.sub(r"\d", "_", a))  # hello_world_
