from flask import request, render_template, Flask, Blueprint, session, redirect, url_for, flash
from ..models import auth

bp = Blueprint('auth', __name__, url_prefix="/auth", template_folder="../templates", static_folder="../static")


@bp.route("/login", methods=['GET','POST'])
def login():
    # if request.method == "POST":
    #     username = request.form.get("username")
    #     password = request.form.get("password")
    #     error = None
    #     user = auth.User.query.filter_by(username=username).first()
    #     if user is None:
    #         error = "用户名错误"
    #     elif password != user.password:
    #         error = "密码错误"
    #     if error is None:
    #         session.clear()
    #         session['user_id'] = user.id
    #         return redirect(url_for("index"))
    #     flash(error)
    return render_template("login.html")


@bp.route("/register", methods=['GET','POST'])
def register():
    if request.method == "POST":
        pass
    return render_template("")
