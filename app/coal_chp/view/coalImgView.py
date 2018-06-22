# -*- coding: utf-8 -*-
from flask import send_from_directory
from . import coalviews
from util.get_all_path import GetPath
import os


# 文件预览
@coalviews.route('/coalimgpreview/<planid>/<filename>', methods=['GET'])
def coalimgpreview(planid, filename):
    return send_from_directory(GetPath.getImgCoalNetDir(planid), filename)

