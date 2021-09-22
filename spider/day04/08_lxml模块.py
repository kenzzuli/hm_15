from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''
# 利用etree.HTML，将字符串转化为Element对象
html = etree.HTML(text)
print(html)  # <Element html at 0x7fa5feebab08>
# 查看Element对象中包含的字符串
# 通过输出结果可以看到，lxml自动补全了html、body、li标签
print(etree.tostring(html))  # byte类型
print(etree.tostring(html, pretty_print=True).decode())  # str类型

# Element对象具有xpath的方法

# 获取class为item-1的li下的a的href
print(html.xpath("//li[@class='item-1']/a/@href"))
# ['link1.html', 'link2.html', 'link4.html']

# 获取class为item-1的li下的a的文本
print(html.xpath("//li[@class='item-1']/a/text()"))
# ['first item', 'second item', 'fourth item']

# 每个li是一条新闻，把url和文本组成字典
urls = html.xpath("//li/a/@href")
texts = html.xpath("//li/a/text()")
assert len(urls) == len(texts)
for url, text in zip(urls, texts):
    tmp_dict = dict()
    tmp_dict["url"] = url
    tmp_dict["title"] = text
    print(tmp_dict)
# {'url': 'link1.html', 'title': 'first item'}
# {'url': 'link2.html', 'title': 'second item'}
# {'url': 'link3.html', 'title': 'third item'}
# {'url': 'link4.html', 'title': 'fourth item'}
# {'url': 'link5.html', 'title': 'fifth item'}

# 有时会出现url或text丢失的情况，导致二者无法一一对应，或对应错误，这时可以先分组，在遍历每一个分组，为每个分组写xpath
text2 = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html"></a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-1"><a>fifth item</a>  
        </ul> </div> '''
html2 = etree.HTML(text2)
# xpath取到li标签，获取包含多个li Element对象的列表
ret2 = html2.xpath("//li[@class='item-1']")
print(ret2)
# [<Element li at 0x7ff1170a3d48>, <Element li at 0x7ff1170a3d88>, <Element li at 0x7ff1170b1048>, <Element li at 0x7ff1170b1088>]
# 遍历列表，对每个Element对象使用xpath方法，取url和href
for element in ret2:
    # print(etree.tostring(element).decode())
    # 注意，对每个li标签使用xpath，要从当前路径开始，即./
    url = element.xpath("./a/@href")
    text = element.xpath("./a/text()")
    # print(url, text)
    tmp_dict = dict()
    url = url[0] if url else None
    text = text[0] if text else None
    tmp_dict["url"] = url
    tmp_dict["title"] = text
    print(tmp_dict)

# {'url': 'link1.html', 'title': None}
# {'url': 'link2.html', 'title': 'second item'}
# {'url': 'link4.html', 'title': 'fourth item'}
# {'url': None, 'title': 'fifth item'}


# 三元运算符 下面三种写法等效
# url = list()
# url = url[0] if url else None
# url = url[0] if len(url) else None
# url = url[0] if len(url) > 0 else None
