# -*- coding: utf-8 -*-
import re
from mark_to_docx import convert
from util.get_all_path import GetPath
from app.models import Plan


pattern = '#+\s'

heading = {
        'heading1': 0,
        'heading2': -1,
        'heading3': -1,
        'heading4': -1,
        'heading5': -1,
        'heading6': -1
    }


def formatHeading():
    heading['heading1'] = 0
    heading['heading2'] = -1
    heading['heading3'] = -1
    heading['heading4'] = -1
    heading['heading5'] = -1
    heading['heading6'] = -1


def updateHeading(current, headId):
    for i in range(1, 6):
        if len(current) == i:
            heading['heading%r' % i] = headId


def ganMenu(planId, userId):
    filename = GetPath.getMdTemplateResult(planId, userId)
    titles = []
    global heading
    global newHeading
    headId = 1
    current = None
    preCurrent = '$'
    parentID = 0
    with open(filename, 'r') as f:
        for i in f.readlines():
            title = {}
            if not re.match(pattern, i.strip(' \t\n')):
                continue
            i = i.strip(' \t\n')
            current = i.split(' ')[0]
            if len(current) < 5:
                # 当前标题级别比前一个小，则当前标题的父类标题是上一个的headId
                # 注释：#越多级别越小
                # 不论大多少个级别，只要父类级别大就是它的父类
                if len(current) > len(preCurrent):
                    parentID = headId - 1
                    # 更新当前级别父类
                    updateHeading(current, parentID)
                # 当前级别比父类级别大，则去heading中寻找记录过的父类级别
                # 注释：#越少级别越大
                elif len(current) < len(preCurrent):
                    length = len(current)
                    # 当在文中出现一级标题的时候还原所有父类级别到初始值
                    if length == 1:
                        formatHeading()
                        # 给当父类结果类赋值
                        parentID = 0
                    else:
                        getVal = heading['heading%r' % length]
                        # 如果有记录过该级别的父类项
                        if getVal != -1:
                            parentID = getVal
                        # 改级别项没有记录则依次向上找父类，指导找到一级标题
                        else:
                            for j in range(length, 1, -1):
                                tempVal = heading['heading%r' % j]
                                if tempVal != -1:
                                    parentID = tempVal
                                    break
                funName = i[len(current):].strip(' \t\n')
                title['FunName'] = funName
                title['FunID'] = headId
                title['ParentID'] = parentID
                titles.append(title)
                preCurrent = current
                headId += 1
    return titles


def addAnchorMark(titles, planId, userId):
    filename = GetPath.getHtmlTemplateResult(planId, userId)
    anchorHtml = u''
    with open(filename, 'r') as f:
        for i in f.readlines():
            for title in titles:
                old = '>' + title['FunName'] + '<'
                new = " id='a_" + str(
                    title['FunID']) + "'>" + title['FunName'] + "<"
                old = old.replace("\r", "")
                i = i.replace(old, new)
            anchorHtml += i.decode('utf8')
    return anchorHtml


# 生成临时md文档和临时html文件
def tempFile(mdvar, htmlvar, planId, userId):
    # 替换url
    # mdvar = mdvar.replace("117.36.73.154", "127.0.0.1", len(mdvar))
    # 用户的html临时文件
    md_path = GetPath.getMdTemplateResult(planId, userId)
    f = open(md_path, 'w')    # r只读，w可写，a追加
    f.write(mdvar)
    f.close()
    # 用户的html临时文件
    html_path = GetPath.getHtmlTemplateResult(planId, userId)
    f = open(html_path, 'w')    # r只读，w可写，a追加
    f.write(htmlvar)
    f.close()


# 执行文件转换操作
def convertdel(planId, userId, mdvar, htmlvar):
    # 用户的md源文件
    report_path = GetPath.getMdTemplateResult(planId, userId)
    # 在源文件后追加表格控制
    with open(report_path, 'a+') as f:
        # f.write(u'|111111 | 111111111111111111111111111111  |1111111111111111111111111111111111111111 |  111111 | 111111 | 11111111111111111111|\n')
        # f.write('| 陕鼓清单 | 陕鼓清单陕鼓清单陕鼓清单陕鼓清单陕鼓清单  | 陕鼓清单陕鼓清单陕鼓清单陕鼓清单陕鼓清单陕鼓清单 |  陕鼓清单 | 陕鼓清单 | 陕鼓清单陕鼓清单陕鼓清单|\n')
        f.write('| ListOfShaanxi | ListOfShaanxiListOfShaanxiListOfShaanxi  | ListOfShaanxiListOfShaanxiListOfShaanxiListOfShaanxi |  ListOfShaanxi | ListOfShaanxi | ListOfShaanxiListOfShaanxi|\n')
    # 空模板文件
    ccppmb_path = GetPath.getDocxTemplateSource("ccppmb.docx")
    # 带全部样式的封皮
    ccppfp_path = GetPath.getDocxTemplateSource("ccppfp.docx")
    # 结果文件
    ccppresult_path = GetPath.getDocxTemplateResult(planId, userId)
    convert.execute(ccppmb_path, ccppfp_path, report_path, ccppresult_path)
    # 恢复文件
    tempFile(mdvar, htmlvar, planId, userId)


MD = []


def createMD(menu, contents):
    formatJson(menu[0]["children"], contents)
    result = MD[:]
    del MD[0:]
    content = "".join(result)
    return content


def formatJson(children, contents):
    for i in range(len(children)):
        # print(children[i])
        for j in range(len(contents)):
            if children[i]["id"] == contents[j]["id"]:
                MD.append(u"#" * len(contents[j]["class"]) + " " +
                          children[i]["text"] + u"\n")
                if contents[j]["content"] != "":
                    MD.append(contents[j]["content"] + u"\n")
                # MD.append(u"#" * len(contents[j]["class"]) + " " +
                #           children[i]["text"] + u"\n" + "#" * 5 + " " +
                #           contents[j]["content"] + u"\n")
        if not children[i]["children"]:
            del children[i]["children"]
        else:
            formatJson(children[i]["children"], contents)
