# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 23:11
# @Author  : ht
# @File    : test.py
# @Software: PyCharm

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from jieba.analyse import  extract_tags
import string
import utils
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    print(jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add}))
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})
get_l2_data()