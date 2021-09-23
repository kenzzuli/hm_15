# 假设下面的内容是从网上抓取的
# 要求：
# 1.将字符串中的空白字符全部去掉
# 2.再使用" "作为分隔符，拼接成一个整齐的字符串

poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\r\n 更上一层楼 \t\r"
print(poem_str)
print(poem_str.split())
# 拼接列表
print(" ".join(poem_str.split()))
# 拼接字符串
print(" ".join("1234"))
# 拼接元组
join_tuple = ("hello", "hi", "fuck")
print(", ".join(join_tuple))
# 拼接字典 此时只拼接了key，且key必须是字符串
join_dic = {"name": "Peter", "age": 18, "sex": True, "1": 1.8, "1.89": 2}
print("$".join(join_dic))

temp_str = "燕子去了，有再来的时候；杨柳枯了，有再青的时候；桃花谢了，有再开的时候。但是，聪明的，你告诉我，" \
           "我们的日子为什么一去不复返呢？——是有人偷了他们罢：那是谁？又藏在何处呢？是他们自己逃走了罢：" \
           "现在又到了哪里呢？我不知道他们给了我多少日子；但我的手确乎是渐渐空虚了。" \
           "在默默里算着，八千多日子已经从我手中溜去；像针尖上一滴水滴在大海里，我的日子滴在时间的流里，没有声音，也没有影子。" \
           "我不禁头涔涔而泪潸潸了。去的尽管去了，来的尽管来着；" \
           "去来的中间，又怎样地匆匆呢？早上我起来的时候，小屋里射进两三方斜斜的太阳。太阳他有脚啊，轻轻悄悄地挪移了；我也茫茫然跟着旋转。" \
           "于是——洗手的时候，日子从水盆里过去；吃饭的时候，日子从饭碗里过去；默默时，便从凝然的双眼前过去。" \
           "我觉察他去的匆匆了，伸出手遮挽时，他又从遮挽着的手边过去，天黑时，我躺在床上，他便伶伶俐俐地从我身上跨过，从我脚边飞去了。"

temp_list = temp_str.split(("；"))

temp2_list = []
for line in temp_list:
    temp2_list.extend(line.split("。"))

temp3_list = []
for line in temp2_list:
    temp3_list.extend(line.split("？"))

temp4_list = []
for line in temp3_list:
    temp4_list.extend(line.split("，"))

temp5_list = []
for line in temp4_list:
    temp5_list.extend(line.split("："))

temp6_list = []
for line in temp5_list:
    temp6_list.extend(line.split("——"))

result_list = []
for line in temp6_list:

    if line != '':
        result_list.append(line)
        print(line)

print(result_list)

test_str = "Ihlovehyouh"
print(test_str.split("h"))
num_list = []
print(type(num_list))
num_str = "0123456789"
num_list.extend(num_str)
num_list.reverse()
print("".join(num_list))