# -*- coding: utf-8 -*-

import xlrd

# f = open('a.txt', 'w')
# import sys
# old = sys.stdout
# # 将当前系统输出储存到一个临时变量中
# sys.stdout = f
# # 输出重定向到文件
boilerlist11 = []
boilerlist13 = []
boilerlist14 = []
boilerlist15 = []
ExcelFile = xlrd.open_workbook(r'data_20171009_10-16.xlsx')

# sheet=ExcelFile.sheet_by_index(1)

sheet = ExcelFile.sheet_by_name(u'锅炉')
for i in range(1, 11):
    rows = sheet.row_values(i)
    del rows[0]
    boilerlist11.append({'engname': u'', 'name': u'' + rows[0].encode("utf-8") + '', 'unit': u'' + rows[1].encode("utf-8") + '', 'remark': u'' + rows[2].encode("utf-8") + ''})

print("# ====================================================")
for i in range(24, 40):
    rows = sheet.row_values(i)
    del rows[0]
    boilerlist13.append({'engname': u'', 'name': u'' + rows[0].encode("utf-8") + '', 'unit': u'' + rows[1].encode("utf-8") + '', 'remark': u'' + rows[2].encode("utf-8") + ''})

print("# ====================================================")
for i in range(41, 53):
    rows = sheet.row_values(i)
    del rows[0]
    boilerlist14.append({'engname': u'', 'name': u'' + rows[0].encode("utf-8") + '', 'unit': u'' + rows[1].encode("utf-8") + '', 'remark': u'' + rows[2].encode("utf-8") + ''})

print("# ====================================================")
for i in range(54, 68):
    rows = sheet.row_values(i)
    del rows[0]
    boilerlist15.append({'engname': u'', 'name': u'' + rows[0].encode("utf-8") + '', 'unit': u'' + rows[1].encode("utf-8") + '', 'remark': u'' + rows[2].encode("utf-8") + ''})
print("# ====================================================")
# # 第三行内容
# # 测试一个打印输出
# sys.stdout = old
# # 还原原系统输出
# f.close()
