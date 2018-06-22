# coding:utf-8
import docx
import sys


def createmd():
    ''''生成md出版文件'''

    document = docx.Document(ur"3333.docx")
    ps = document.tables
    maxi = len(ps)
    print(maxi)
    bs = ['a', 'b', 'c', 'c1', 'd', 'e1', 'e2', 'e3', 'f', 'g', 'h', 'i', 'j', 'k']
    bsdir = {'a': u'燃气轮机发电机组', 'b': u'汽轮发电机组及辅助设备',
             'c': u'余热锅炉', 'c1': u'余热锅炉辅机', 'd': u'分散控制系统', 'e1': u'水系统', 'e2': u'循环水冷却系统',
             'e3': u'废水处理系统', 'f': u'循环水冷却系统', 'g': u'厂用/仪表用压缩空气系统',
             'h': u'往复式发动机发电机组', 'i': u'电气设备', 'j': u'实验室设备', 'k': u'其它设备'}
    # # 遍历每段，在每段中执行替换动作
    f = open('equipmentccpp.json', 'w')
    old = sys.stdout
    # 将当前系统输出储存到一个临时变量中
    sys.stdout = f
    uidjson = u'"equipment_uid": ['
    namejson = u'"equipment_name": ['
    typejson = u'"equipment_type": ['
    contentjson = u'"equipment_content": ['
    unitjson = u'"equipment_unit": ['
    countjson = u'"equipment_count": ['
    remarkjson = u'"equipment_remark": ['
    for tn in ps:
        for i in range(0, len(tn.rows)):
            if tn.rows[i].cells[0].text in bs:
                uidjson += u'"' + str(i) + u'", '
                typejson += u'"' + tn.rows[i].cells[0].text + u'", '
                namejson += u'"' + tn.rows[i].cells[1].text + u'", '
                contentjson += u'"' + tn.rows[i].cells[2].text + u'", '
                unitjson += u'"' + tn.rows[i].cells[4].text + u'", '
                countjson += u'"' + tn.rows[i].cells[3].text + u'", '
                remarkjson += u'"' + tn.rows[i].cells[5].text + u'", '
        uidjson += u'], '
        namejson += u'], '
        typejson += u'], '
        contentjson += u'], '
        unitjson += u'], '
        countjson += u'], '
        remarkjson += u']'
    print("{")
    print(uidjson.encode('utf-8'))
    print(namejson.encode('utf-8'))
    print(typejson.encode('utf-8'))
    print(contentjson.encode('utf-8'))
    print(unitjson.encode('utf-8'))
    print(countjson.encode('utf-8'))
    print(remarkjson.encode('utf-8'))
    print("}")
    sys.stdout = old
    f.close()


def main():
    createmd()


if __name__ == '__main__':
    main()
