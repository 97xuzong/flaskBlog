from flask import Blueprint,render_template

"""
# 蓝图就相当于一个子路由 与app共有一个父类  属于兄弟类
  然后将蓝图注册拼接到 app 主路由上  相当于一个小弟
"""
bp = Blueprint("blog", __name__, url_prefix="/blog",
               static_folder="static", template_folder="templates")


@bp.route("/")
def index():
    posts = [1,2,3,4,5,6]
    return render_template("base.html",posts=posts)
