import functools

from flask import request, render_template, Flask, Blueprint, session, redirect, url_for, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
from RealProject import db
from ..models import auth
from ..forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__, url_prefix="/auth", template_folder="../templates", static_folder="../static")


# 后台登录权限控制
def login_required(view):
    # 限制必须登录才能访问的页面装饰器
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    # 每个请求之前都回去session中查看user_id来获取用户
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = auth.User.query.get(int(user_id))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # 登录视图
    # form = LoginForm(meta={'csrf': False}) # 禁用csrf
    form = LoginForm()
    if form.validate_on_submit():
        user = auth.User.query.filter_by(username=form.username.data).first()
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('blog.index'))
    return render_template('login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    # 注册视图
    form = RegisterForm()
    if form.validate_on_submit():
        user = auth.User(username=form.username.data, password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('blog.index'))
    return render_template('register.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
