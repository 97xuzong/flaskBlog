from flask import request, render_template, Flask, Blueprint, session, redirect, url_for, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
from RealProject import db
from ..models import auth

bp = Blueprint('auth', __name__, url_prefix="/auth", template_folder="../templates", static_folder="../static")


@bp.before_app_request
def load_logged_in_user():
    # 每个请求之前都回去session中查看user_id来获取用户
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = auth.User.query.get(int(user_id))


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None
        user = auth.User.query.filter_by(username=username).first()
        if user is None:
            error = "用户名错误"
        elif not check_password_hash(user.password, password):
            error = "密码错误"
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for("blog.index"))
        flash(error)
    return render_template("login.html")


@bp.route("/register", methods=['GET', 'POST'])
def register():
    # 注册视图
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password1 = request.form['password1']

        if password != password1:
            flash('两次密码输入不一致！')
            return redirect(url_for('auth.register'))

        exists_user = auth.User.query.filter_by(username=username).first()
        if exists_user:
            flash('该用户名已经存在，请更换其他用户名！')
            return redirect(url_for('auth.register'))
        else:
            user = auth.User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            session.clear()
            session['user_id'] = user.id
        return redirect(url_for('blog.index'))
    return render_template('register.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
