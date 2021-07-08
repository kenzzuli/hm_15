# from hm_01_测试模块1 import say_hello
# 如果从多个模块导入同名的工具，后导入的工具会覆盖先导入的工具
# 如果两个同名的工具都想要，可以给其中一个工具起别名 通过别名调用
from hm_02_测试模块2 import say_hello as module2_say_hello
from hm_01_测试模块1 import say_hello


say_hello()
module2_say_hello()