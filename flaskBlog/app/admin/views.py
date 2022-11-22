#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : views.py
# @Time    : 2022/11/22 9:48
# @Software: PyCharm
# @function: 后台视图
from unicodedata import name
from flask import Flask, Blueprint, request, url_for, redirect, render_template, flash
from ..auth.views.register_login import login_required
from RealProject import db

bp = Blueprint("admin", __name__, url_prefix="/admin", static_folder="static", template_folder="templates")


@bp.route('/')
@login_required
def index():
    # 后台主页视图
    return render_template("index.html")
