# -*- coding: utf-8 -*-
from app.ccpp.service.imgdealwith import ccppimglistresult
from app.ccpp.models.ccpp_ccpp_calculateModel import Ccpp_ccpp
from app.ccpp.models.ccpp_turbineModel import CcppTurbine
from util.get_all_path import GetPath
from app.ccpp import gl
from app.models import MyException
import os


class CcppImgService():

    def imgCreate(self, plan_id, user_id):
        # 删除文件
        self.deletebyPlanIdandUserId(plan_id, user_id)
        # 创建文件
        ccpp = Ccpp_ccpp.search_ccpp_ccpp(plan_id)
        ccppTurbine = CcppTurbine.search_CcppTurbine(plan_id)
        ccppimglistresult.imgdealwithExecute(ccpp, ccppTurbine, plan_id, user_id)
        return ccpp, ccppTurbine

    # 根据plan_id删除照片
    def deletebyPlanIdandUserId(self, plan_id, user_id):
        imgPath = GetPath.getImgCcppResultDir(plan_id)
        if imgPath is not None and os.path.exists(imgPath):
            gl.del_file(imgPath)

    # 获得存放ImgDict对象的img列表
    def getImgList(self, planId, userId, targetpath, areadyexistfilenamelist):
        # 获得图像存储目录
        path = GetPath.getImgCcppResultDir(planId)
        imglist = []
        imgnamealllist = []
        # 遍历目录下的所有文件
        for i in os.listdir(path):
            imgDir = {}
            if targetpath == "html" and len(imglist) == 2:
                break
            path_file = os.path.join(path, i)  # 取文件绝对路径
            if os.path.isfile(path_file):
                dirname, filename = os.path.split(path_file)
                chineseName, filenameprefix = self.getChineseName(filename)
                if chineseName is not None:
                    netPath = GetPath.getImgCcppNetPath(filenameprefix, planId, userId)
                    dirname, netfilename = os.path.split(netPath)
                    # 为下次获取到不重复的照片记录已经获取过得照片名称
                    imgnamealllist.append(filename)
                    # 当同一个方案不同人生成图像后，此处会产生重复的图像，
                    # 因为图像的命名和userid有关，
                    # 所以当前的网络地址可判断是否是当前用户产生的图像，
                    # 故去重
                    if filename == netfilename and filename not in areadyexistfilenamelist:
                        imgDir['chineseName'] = chineseName
                        imgDir['netPath'] = netPath
                        imgDir['filename'] = filename
                        imglist.append(imgDir)
        return imglist, imgnamealllist

    def getChineseName(self, filename):
        if filename is not None and filename.find("db") != -1:
            return u"单压余热锅炉+背压汽轮机图示", "db"
        if filename is not None and filename.find("dc") != -1:
            return u"单压余热锅炉+抽凝汽轮机图示", "dc"
        if filename is not None and filename.find("dn") != -1:
            return u"单压余热锅炉图示", "dn"
        if filename is not None and filename.find("sbq") != -1:
            return u"双压余热锅炉+补凝汽轮机图示", "sbq"
        if filename is not None and filename.find("sb") != -1:
            return u"双压余热锅炉+背压汽轮机图示", "sb"
        if filename is not None and filename.find("sc") != -1:
            return u"双压余热锅炉+抽凝汽轮机图示", "sc"
        if filename is not None and filename.find("sn") != -1:
            return u"双压余热锅炉图示", "sn"
        return None
    
    def getccppimginfo(self, ccpp, ccppTurbine, planId, user_id):
        if ccpp is None:
            ccpp = Ccpp_ccpp.search_ccpp_ccpp(planId)
        if ccppTurbine is None:
            ccppTurbine = CcppTurbine.search_CcppTurbine(planId)
        if ccpp is None or ccppTurbine is None:
            return 'is not ccpp'
        if ccpp.boiler_single_or_dula_pressure_design == "singlepot" and ccppTurbine.s_steam_type_test == 2:
            path = GetPath.getImgCcppNetPath('db', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 单压余热锅炉+背压汽轮机图示'
            else:
                raise MyException("dbPathNotFond",
                                  u"单压余热锅炉+背压汽轮机图找不到,请检查数据或者网络是否有误。",
                                  path + u"单压余热锅炉+背压汽轮机图找不到,请查看生成图片代码，或者目录结构是否完整。",
                                  path)
        elif ccpp.boiler_single_or_dula_pressure_design == "singlepot" and ccppTurbine.s_steam_type_test == 1:
            path = GetPath.getImgCcppNetPath('dc', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 单压余热锅炉+抽凝汽轮机图示'
            else:
                raise MyException("dcPathNotFond",
                                  u"单压余热锅炉+抽凝汽轮机图找不到,请检查数据或者网络是否有误。",
                                  path + u"单压余热锅炉+抽凝汽轮机图找不到,请查看生成代码，或者目录结构是否完整。",
                                  path)
        elif ccpp.boiler_single_or_dula_pressure_design == "singlepot" and ccppTurbine.s_steam_type_test is None:
            path = GetPath.getImgCcppNetPath('dn', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 单压余热锅炉图示'
            else:
                raise MyException("dnPathNotFond",
                                  u"单压余热锅炉图找不到,请检查数据或者网络是否有误。",
                                  path + u"单压余热锅炉图找不到,请查看生成代码，或者目录结构是否完整。",
                                  path)
            
        elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test == 3:
            path = GetPath.getImgCcppNetPath('sbq', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 双压余热锅炉+补凝汽轮机图示'
            else:
                raise MyException("sbqPathNotFond",
                                  u"双压余热锅炉+补凝汽轮机图找不到,请检查数据或者网络是否有误。",
                                  path + u"双压余热锅炉+补凝汽轮机图找不到,请查看生成代码，或者目录结构是否完整。",
                                  path)
            
        elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test == 2:
            path = GetPath.getImgCcppNetPath('sb', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 双压余热锅炉+背压汽轮机图示'
            else:
                raise MyException("sbPathNotFond",
                                  u"双压余热锅炉+背压汽轮机图找不到,请检查数据或者网络是否有误。",
                                  path + u"双压余热锅炉+背压汽轮机图找不到,请查看生成代码，或者目录结构是否完整。",
                                  path)
            
        elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test == 1:
            path = GetPath.getImgCcppNetPath('sc', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 双压余热锅炉+抽凝汽轮机图示'
            else:
                raise MyException("scPathNotFond",
                                  u"双压余热锅炉+抽凝汽轮机生成资源图找不到,请检查数据或者网络是否有误。",
                                  path + u"双压余热锅炉+抽凝汽轮机生成资源图找不到,请查看生成代码，或者目录结构是否完整。",
                                  path)
            
        elif ccpp.boiler_single_or_dula_pressure_design == "doublepot" and ccppTurbine.s_steam_type_test is None:
            path = GetPath.getImgCcppNetPath('sn', planId, user_id)
            if path is not None:
                return u'# 附件一 图纸\n##### ![](' + path + u')\n##### 双压余热锅炉图示'
            else:
                raise MyException("snPathNotFond",
                                  u"双压余热锅炉生成资源图找不到,请检查数据或者网络是否有误。",
                                  path + u"双压余热锅炉生成资源图找不到,请查看生成代码，或者目录结构是否完整。",
                                  path)
        return None

