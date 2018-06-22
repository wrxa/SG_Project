# -*- coding=utf-8 -*-
import lxml
from lxml import etree
from xml.etree.ElementTree import ElementTree,Element
import os


#   读取并解析xml文件
#     in_path: xml路径
#     return: ElementTree
def read_xml(in_path):

    tree = ElementTree()
    tree.parse(in_path)
    return tree


#   '''判断某个节点是否包含所有传入参数属性
#     node: 节点
#     kv_map: 属性及属性值组成的map'''
def if_match(node, kv_map):

    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


#---------------search -----
#   '''查找某个路径匹配的所有节点
#     tree: xml树
#     path: 节点路径'''
def find_nodes(tree, path):
    return tree.findall(path)


#   '''根据属性及属性值定位符合的节点，返回节点
#     nodelist: 节点列表
#     kv_map: 匹配属性及属性值map'''
def get_node_by_keyvalue(nodelist, kv_map):
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


#   '''将xml文件写出
#     tree: xml树
#     out_path: 写出路径'''
def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


#   '''根据属性及属性值定位符合的节点，返回节点
#     nodelist: 节点列表
#     kv_map: 匹配属性及属性值map'''
def get_node_by_keyvalue(nodelist, kv_map):
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


#---------------change -----
#   '''修改/增加 /删除 节点的属性及属性值
#     nodelist: 节点列表
#     kv_map:属性及属性值map'''
def change_node_properties(nodelist, kv_map, is_delete=False):
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))

#       '''改变/增加/删除一个节点的文本
#     nodelist:节点列表
#     text : 更新后的文本'''
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


#   '''新造一个节点
#     tag:节点标签
#     property_map:属性及属性值map
#     content: 节点闭合标签里的文本内容
#     return 新节点'''
def create_node(tag, property_map, content):

    element = Element(tag, property_map)
    element.text = content
    return element


#   '''给一个节点添加子节点
#     nodelist: 节点列表
#     element: 子节点'''
def add_child_node(nodelist, element):
    for node in nodelist:
        node.append(element)


#   '''同过属性及属性值定位一个节点，并删除之
#     nodelist: 父节点列表
#     tag:子节点标签
#     kv_map: 属性及属性值列表'''
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    for parent_node in nodelist:
        children = parent_node.getchildren()
    for child in children:
        if child.tag == tag and if_match(child, kv_map):
            parent_node.remove(child)





if __name__ == "__main__":

    image3path = "D:\\py_buffer\\docx_Pro\\test3\\word\\media\\"
    image3num = (sum([len(x) for _, _, x in os.walk(os.path.dirname(image3path))]))

    xml3path = "D:\\py_buffer\\docx_Pro\\test3\\word\\"
    xmldoc3path = xml3path + 'document.xml'
    xml_rels3path = xml3path + "_rels\\document.xml.rels"


    #1. 读取xml文件
    tree = read_xml(xml3path + "document.xml")

    print(tree)
    w = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    xmlns = '{http://schemas.openxmlformats.org/package/2006/content-types}'
    wp = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
    a = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    uri = "{http://schemas.openxmlformats.org/drawingml/2006/picture}"
    pic = "{http://schemas.openxmlformats.org/drawingml/2006/picture}"
    r = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
    #命名空间 和 XPath 搭配使用 报错


    #2. 属性修改
    #A. 找到父节点
    nodes = find_nodes(tree, w+"body"
                       +'/'+w+'p'
                       +'/'+w+'r'
                       +'/'+w+'drawing'
                       +'/'+wp+'anchor'
                       +'/'+a+'graphic'
                       +'/'+a+'graphicData'
                       +'/'+pic+'pic'
                       +'/'+pic+'blipFill'
                       +'/'+a+'blip')
    #SyntaxError:prefix 'w' not found in prefix map

    print(nodes)
    i = 0
    key = r + 'embed'
    for node in nodes:
        print(node.get(key))

    i = 1
    for node in nodes:
        del node.attrib[key]
        node.set(key, 'rId10'+str(i))
        i += 1

    write_xml(tree, xmldoc3path)

    tree = read_xml(xml_rels3path)
    # <Relationship Target="media/image1.png" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Id="rId4"/>
    xmlns = "{http://schemas.openxmlformats.org/package/2006/relationships}"

    node = tree.getroot()
    # print(node)
    for i in range(image3num):

        element = Element(xmlns + 'Relationship')
        if i == 0:
            element.set('Target', "media/image" + str(i+1) + ".jpeg")
        else:
            element.set('Target', "media/image" + str(i+1) + ".png")
        element.set('Type', "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
        element.set('Id', "rId10" + str(i+1))
        node.append(element)

    write_xml(tree, xml_rels3path)

        # #B. 通过属性准确定位子节点
    # result_nodes = get_node_by_keyvalue(nodes, {"name":"BProcesser"})
    # #C. 修改节点属性
    # change_node_properties(result_nodes, {"age": "1"})
    # #D. 删除节点属性
    # change_node_properties(result_nodes, {"value":""}, True)
    #
    # #3. 节点修改
    # #A.新建节点
    # a = create_node("person", {"age":"15","money":"200000"}, "this is the firest content")
    # #B.插入到父节点之下
    # add_child_node(result_nodes, a)
    #
    # #4. 删除节点
    # #定位父节点
    # del_parent_nodes = find_nodes(tree, "processers/services/service")
    # #准确定位子节点并删除之
    # target_del_node = del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency" : "chain1"})
    #
    # #5. 修改节点文本
    # #定位节点
    # text_nodes = get_node_by_keyvalue(find_nodes(tree, "processers/services/service/chain"), {"sequency":"chain3"})
    # change_node_text(text_nodes, "new text")
    #
    # #6. 输出到结果文件
    # write_xml(tree, "./out.xml")