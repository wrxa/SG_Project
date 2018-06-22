# -*- coding:UTF-8 -*-
from config import config
import os
# from flask_login import current_user

'''
获取所有文件操作的路径:方便管理文件的命名规则
判断是否存在一个目录，如果不存在创建
'''


def getpathbyos(path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.join(os.getcwd(), path, filename)


class GetPath(object):
    '''
    获取图像处理-CCPP资源物理路径
    路径："app/ccpp/service/imgdealwith/ccppimg"
    filename: 文件名
    '''
    @staticmethod
    def getImgCcppSource(filename):
        sourceDir = config['imgConfig'].CCPP_IMG_PATH_SOURCE
        return getpathbyos(sourceDir, filename)

    '''
    获取图像处理-coal资源物理路径
    路径："app/coal_chp/service/imgProcessing/model"
    filename: 文件名
    '''
    @staticmethod
    def getCoalimgpath(filename):
        sourceDir = config['imgConfig'].COAL_IMG_PATH_SOURCE
        modelName = filename + ".png"
        return getpathbyos(sourceDir, modelName)

    '''
    获取图像处理-CCPP处理结果物理路径
    路径："app/coal_chp/service/imgProcessing/result"
    filename: 文件名
    '''
    @staticmethod
    def getImgCoalResult(filename, planId):
        sourceDir = config['imgConfig'].COAL_IMG_PATH_RESULT
        # 生成文件命名规则
        # userId = current_user.id
        resultName = filename + "_" + str(planId) + ".png"
        return getpathbyos(sourceDir + '/' + str(planId), resultName)

    @staticmethod
    def getImgCoalResultDir(planId=None):
        sourceDir = config['imgConfig'].COAL_IMG_PATH_RESULT
        if planId is not None:
            return getpathbyos(sourceDir + '/' + str(planId), '')
        else:
            return getpathbyos(sourceDir, '')

    '''
    获取图像处理-CCPP处理结果物理路径
    路径："app/ccpp/service/imgdealwith/resultimg"
    filename: 文件名
    '''
    @staticmethod
    def getImgCcppResult(filenameprefix, planId, userId):
        sourceDir = config['imgConfig'].CCPP_IMG_PATH_RESULT
        # 生成文件命名规则
        return getpathbyos(sourceDir + '/' + str(planId), filenameprefix + str(planId) + u"-" + str(userId) + u".png")

    @staticmethod
    def getImgCcppResultDir(planId=None):
        sourceDir = config['imgConfig'].CCPP_IMG_PATH_RESULT
        if planId is not None:
            return getpathbyos(sourceDir + '/' + str(planId), '')
        else:
            return getpathbyos(sourceDir, '')

    @staticmethod
    def getImgGPGResultDir(planId):
        sourceDir = config['imgConfig'].GPG_IMG_PATH_RESULT
        if planId is not None:
            return getpathbyos(sourceDir + '/' + str(planId), '')
        else:
            return getpathbyos(sourceDir, '')

    # 获得生物质图片路径
    @staticmethod
    def getImgBiomassResultDir(planId):
        sourceDir = config['imgConfig'].BIOMASS_IMG_PATH_RESULT
        if planId is not None:
            # return getpathbyos(sourceDir + '/' + str(planId), '')
            return getpathbyos(sourceDir, '')
        else:
            return getpathbyos(sourceDir, '')

    # 获取图像处理-生物质处理结果网络路径
    @staticmethod
    def getImgBiomassNetPath(filenameprefix, planId):
        sourceDir = config['imgConfig'].BIOMASS_IMG_PATH_RESULT
        path = getpathbyos(sourceDir + '/', filenameprefix + '_' + str(planId) + u'.png')

        if os.path.exists(path):
            return u'http://' + config['ipandport'].APP_IP + u':' + config['ipandport'].APP_PORT + \
                u'/biomassimgpreview/' + filenameprefix + '_' + str(planId) + u'.png'
        else:
            return None

    '''
    获取图像处理-Coal处理结果网络路径
    filenameprefix: 前缀
    planId: 方案ID
    userId: 用户ID
    '''
    @staticmethod
    def getImgCoalNetPath(imgName, planId):
        path = GetPath.getImgCoalResult(imgName, planId)
        if os.path.exists(path):
            return u'http://' + config['ipandport'].APP_IP + u':' + config['ipandport'].APP_PORT + u'/coalimgpreview/' + str(planId) + '/'+imgName + '_' + str(planId) + u'.png'
        else:
            return None

    '''
    获取网络地址对应的物理目录：coalimgpreview使用
    '''
    @staticmethod
    def getImgCoalNetDir(planId):
        return os.path.join(os.getcwd(), config['imgConfig'].COAL_IMG_PATH_RESULT + "/" + str(planId), "")



    '''
    获取图像处理-CCPP处理结果网络路径
    filenameprefix: 前缀
    planId: 方案ID
    userId: 用户ID
    '''
    @staticmethod
    def getImgCcppNetPath(filenameprefix, planId, userId):
        path = GetPath.getImgCcppResult(filenameprefix, planId, userId)
        if os.path.exists(path):
            return u'http://' + config['ipandport'].APP_IP + u':' + config['ipandport'].APP_PORT + \
                u'/ccpp/ccppimgpreview/' + str(planId) + '/' + filenameprefix + str(planId) + u"-" + str(userId) + u'.png'
        else:
            return None
    
    '''
    获取网络地址对应的物理目录：ccppimgpreview使用
    '''
    @staticmethod
    def getImgCcppNetDir(planId):
        return os.path.join(os.getcwd(), config['imgConfig'].CCPP_IMG_PATH_RESULT + "/" + str(planId), "")

    '''
    获取图像处理-GPG处理结果网络路径
    filenameprefix: 前缀
    planId: 方案ID
    '''
    @staticmethod
    def getImgGPGNetPath(filenameprefix, planId):
        sourceDir = config['imgConfig'].GPG_IMG_PATH_RESULT
        path = getpathbyos(sourceDir + '/' + str(planId), filenameprefix + '_' + str(planId) + u'.png')

        if os.path.exists(path):
            return u'http://' + config['ipandport'].APP_IP + u':' + config['ipandport'].APP_PORT + \
                u'/gpgimgpreview/' + str(planId) + '/' + filenameprefix + '_' + str(planId) + u'.png'
        else:
            return None

    '''
    获取excle处理-CCPP经济性分析资源物理路径
    路径："app/ccpp/service/excledealwith/ccppbaseexcle"
    full_year:全投资收益率（集团规定）计算年数
    depreciation_years:折旧摊销年限
    '''
    @staticmethod
    def getExcleCcppSource(full_year, depreciation_years, filename='economicccpp.xlsx'):
        sourceDir = config['excleConfig'].CCPP_EXCLE_ECONOMIC_PATH_SOURCE
        if full_year is not None and depreciation_years is not None:
            filename = u'economicccpp-' + str(int(depreciation_years)) + u'-' + full_year + u'.xlsx'
        return getpathbyos(sourceDir, filename)

    '''
    为ccpp经济性分析结果文件下载配置文件名称
    和getExcleCcppResult使用的文件名称保持一致
    '''
    @staticmethod
    def getExcleCcppResultFileName(planId, userId):
        return str(planId) + u"-" + str(userId) + u"-economicccpp.xlsx"

    '''
    获取excle处理-CCPP经济性分析处理结果物理路径
    路径："app/ccpp/service/excledealwith/economicresultexcle"
    '''
    @staticmethod
    def getExcleCcppResult(planId, userId):
        sourceDir = config['excleConfig'].CCPP_EXCLE_ECONOMIC_PATH_RESULT
        return getpathbyos(sourceDir, GetPath.getExcleCcppResultFileName(planId, userId))

    '''
    获取模板生成处理-共通md文件物理路径
    '''
    @staticmethod
    def getMdTemplateResult(planId, userId):
        sourceDir = config['markToDocx'].MAIN_INPUTFILE_MD_PATH
        return getpathbyos(sourceDir, u"planReport_" + str(planId) + u"-" + str(userId) + u".md")

    '''
    获取模板生成处理-共通html文件物理路径
    '''
    @staticmethod
    def getHtmlTemplateResult(planId, userId):
        sourceDir = config['markToDocx'].MAIN_INPUTFILE_HTML_PATH
        return getpathbyos(sourceDir, u"planReport_" + str(planId) + "-" + str(userId) + u".html")

    '''
    获取模板生成处理-共通docx资源文件物理路径
    '''
    @staticmethod
    def getDocxTemplateSource(filename):
        sourceDir = config['markToDocx'].MAIN_SOURCE_DOCX_PATH
        return getpathbyos(sourceDir, filename)

    '''
    获取模板生成处理-共通docx结果文件名称
    '''
    @staticmethod
    def getDocxTemplateResultFilename(planId, userId):
        return str(planId) + u"-" + str(userId) + u".docx"

    '''
    获取模板生成处理-共通docx结果文件物理路径
    '''
    @staticmethod
    def getDocxTemplateResult(planId, userId):
        sourceDir = config['markToDocx'].MAIN_OUTFILE_FOR_DOWNLOAD_DOCX_PATH
        return getpathbyos(sourceDir, GetPath.getDocxTemplateResultFilename(planId, userId))

    '''
    获取模板生成处理-共通static文件夹下img文件物理路径
    '''
    @staticmethod
    def getImgMainSource(filename):
        sourceDir = config['imgConfig'].MAIN_IMG_PATH
        return getpathbyos(sourceDir, filename)

    '''
    获取模板生成处理-共通static文件夹下img文件网络路径
    '''
    @staticmethod
    def getImgMainNet(filename):
        return u'http://' + config['ipandport'].APP_IP + u':' + config['ipandport'].APP_PORT + \
               u'/uploaded_file/' + filename + u''


def main():
    pass


if __name__ == '__main__':
    main()
