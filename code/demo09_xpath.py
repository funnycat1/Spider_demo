"""
xpath 是在 XML 文档中搜索内容的一门语言
html 是 xml 的一个子集

pip install lxml

"""

from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>没头脑</nick>
        </div>
        <span>
            <nick>不高兴</nick>
            <div>
                <nick>小糊涂</nick>
            </div>
        </span>
    </author>
    
    <partner>
        <nick id="dlm">大脸猫</nick>
        <nick id="lps">蓝皮鼠</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)

# / 表示层级关系，第一个 / 是根节点
name_result = tree.xpath("/book/name/text()")  # text() 拿到文本，返回 list
print(name_result)  # ['野花遍地香']

nick_result = tree.xpath("/book/author/nick/text()")
print(nick_result)  # ['周大强', '周芷若', '周杰伦', '蔡依林']

nick_result = tree.xpath("/book/author//nick/text()")  # // 所有子代 nick
print(nick_result)  # ['周大强', '周芷若', '周杰伦', '蔡依林', '没头脑', '不高兴', '小糊涂']

nick_result = tree.xpath("/book/author/*/nick/text()")  # * 匹配一个子代
print(nick_result)  # ['没头脑', '不高兴']

nick_result = tree.xpath("/book//nick/text()")  # book 下所有的 nick
print(nick_result)  # ['臭豆腐', '周大强', '周芷若', '周杰伦', '蔡依林', '没头脑', '不高兴', '小糊涂', '大脸猫', '蓝皮鼠']
