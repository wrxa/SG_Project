# coding:utf-8
import docx
from docx.enum.style import WD_STYLE_TYPE

''''生成所有的表格样式'''
document = docx.Document(ur"123456456456.docx")
document.save(u"1111111111111111111111111111111.docx")
# styles = document.styles
# paragraphs = document.paragraphs
# # 遍历每段，在每段中执行替换动作
# for para in paragraphs:
#     print(para.style.name)
# 生成所有表样式
# for s in styles:
#     if s.type == WD_STYLE_TYPE.CHARACTER:
#         print(s.name)
