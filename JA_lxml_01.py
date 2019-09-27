from lxml import etree

text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">张三</a></li>
        <li class="item-1"><a href="link2.html"></a>李四</li>
        <li.class="item-inative"><a href="link3.html">王五</a></li>
        <li class="item-1"><a href="link4.html">赵六</a></li>
        <li class="item-0"><a href="link5.html">老七</a></li>
    </ul>
</div>
"""

# etree.HTML()将字符串解析为特殊的HTML对象
html = etree.HTML(text)

# 将HTML对象转换成字符串
result = etree.tostring(html, encoding="utf-8").decode()

print(result)
