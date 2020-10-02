import parsel


"""
parsel是一款高性能的Python HTML/XML解析器，将字符串转换为Selector对象，Selector对象具有xpath的方法，
返回结果是列表,能够接收bytes类型的数据和str类型的数据，我们可以利用xpath来快速定位特定元素以及获取节点信息
"""


html_str = """
            <div>
                <ul>
                    <li class="item-1">
                        <a href="link1.html">第一个</a>
                    </li>
                    <li class="item-2">
                        <a href="link2.html">第二个</a>
                    </li>
                    <li class="item-3">
                        <a href="link3.html">第三个</a>
                    </li>
                    <li class="item-4">
                        <a href="link4.html">第四个</a>
                    </li>
                    <li class="item-5">
                        <a href="link5.html">第五个</a>
                    </li>
                </ul>
            </div>                 
"""

# 1 先将html_str字符串转换为Selector对象
data = parsel.Selector(html_str)
# print(data)

# 2 从根节点开始，获取所有<a>标签
result1 = data.xpath('/html/body/div/ul/li/a').extract()

# 3 跨节点获取所有<a>标签
result2 = data.xpath('//a').extract()

# 4 选取当前节点    使用场景：需要对选取的标签的下一级标签进行多次提取
result3 = data.xpath('//ul')
result4 = result3.xpath('./li/a').extract()

# 5 选取当前节点的父节点，获取父节点的class属性值
result5 = data.xpath('//a')
result6 = result5.xpath('../@class').extract()

# 6 获取第三个<li>标签的节点（有两种方法）
result7 = data.xpath('//li[3]').extract()
result8 = data.xpath('//li')[2].extract()

# 7 通过定位属性的方法获取第四个<a>标签
result9 = data.xpath('//a[@href="link4.html"]').extract()

# 8 用属性定位标签，获取第四个<a>标签包裹的文本信息
result10 = data.xpath('//a[@href="link4.html"]/text()').extract()

# 9 获取第五个<a>标签href的属性值
result11 = data.xpath('//li[5]/a/@href').extract()

print(result11)