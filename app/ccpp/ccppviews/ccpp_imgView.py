# -*- coding: utf-8 -*-
from flask import render_template, session, send_from_directory, request, jsonify
from flask_login import login_required, current_user
from . import ccppviews
from util.get_all_path import GetPath
from app.ccpp.service.ccpp_imgService import CcppImgService
from flask import current_app


# 文件预览
@ccppviews.route('/ccppimgpreview/<planid>/<filename>', methods=['GET'])
def ccppimgpreview(planid, filename):
    return send_from_directory(GetPath.getImgCcppNetDir(planid), filename)


# 进入ccpp_ccpp参数调研界面
@ccppviews.route('/toccppimg')
@login_required
def toccppimg():
    current_app.logger.warning(u'生成前2张图像 (%d planId)', session.get('planId'))
    # 生成图纸
    planId = session.get('planId')
    user_id = current_user.id
    # 生成前2张
    CcppImgService().imgCreate(planId, user_id)
    # 获取地址列表
    imglist, imgnamelist = CcppImgService().getImgList(planId, user_id, "html", [])
    return render_template(
        'page/ccpp/ccpp_img.html',
        imglist=imglist,
        imglength=len(imglist))


# 文件下载
@ccppviews.route("/downloadimg", methods=['GET'])
@login_required
def downloadimg():
    filename = request.values.get('filename')
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    dirpath = GetPath.getImgCcppResultDir(session.get('planId'))
    # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True)
    # as_attachment=True 一定要写，不然会变成打开，而不是下载


# 文件下载
@ccppviews.route("/selflog/<filename>", methods=['GET'])
def log(filename):
    return send_from_directory("../", filename, as_attachment=True)


# 文件打包下载
@ccppviews.route("/packagdownload", methods=['GET'])
@login_required
def packagdownload():
    # 将文件夹压缩
    # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(GetPath.getImgCcppResultDir(), str(session.get('planId')), as_attachment=True)
    # as_attachment=True 一定要写，不然会变成打开，而不是下载


@ccppviews.route("/getSurplusImg", methods=['POST'])
@login_required
def getSurplusImg():
    planId = session.get('planId')
    current_app.logger.warning(u'生成前后续图像 (%d planId)', planId)
    user_id = current_user.id
    # 为生成后续的图像
    imglist, imgnameprelist = CcppImgService().getImgList(planId, user_id, "html", [])
    # 生成后续的图像
    imglist, imgnamelist = CcppImgService().getImgList(planId, user_id, "js", imgnameprelist)
    return jsonify({'imglist': imglist, 'imgnamelist': imgnamelist, 'imgnameprelist': imgnameprelist})
