#  -*- coding: utf-8 -*-
# @Author  : xuwengang
# @File    : views.py
# @Time    : 2022/11/22 9:48
# @Software: PyCharm
# @function: 后台视图

from flask import Flask, Blueprint, request, url_for, redirect, render_template, flash

from .forms import CategoryForm, PostForm, TagForm
from ..auth.views.register_login import login_required
from RealProject import db
from ..blog.models import Category, Post, Tag

bp = Blueprint("admin", __name__, url_prefix="/admin",
               static_folder="static", template_folder="templates")


@bp.route('/')
@login_required
def index():
    # 后台主页视图
    return render_template("admin/index.html")


@bp.route('/category')
@login_required
def category():
    # 查看分类
    page = request.args.get('page', 1, type=int)
    # 分页处理
    pagination = Category.query.order_by(-Category.add_date).paginate(page=page, per_page=5, error_out=False)
    category_list = pagination.items
    print("页对象的数据", category_list)
    return render_template('admin/category.html', category_list=category_list, pagination=pagination)


@bp.route('/category/add', methods=["GET", "POST"])
@login_required
def category_add():
    # 新增分类
    form = CategoryForm()
    if form.validate_on_submit():  # 自动判断请求方法
        category = Category(name=form.name.data, icon=form.icon.data)
        db.session.add(category)
        db.session.commit()
        flash(f"分类>{category.name}保存成功")
        return redirect(url_for("admin.category"))
    return render_template("admin/category_form.html", form=form)


@bp.route('/category/edit/<int:cate_id>', methods=["GET", "POST"])
@login_required
def category_edit(cate_id):
    # 修改分类  : 需要传递一个主键值
    # 将数据回显到表单中
    category = Category.query.get(cate_id)  # get方法中的入参为主键值
    form = CategoryForm(name=category.name, icon=category.icon)
    if form.validate_on_submit():
        # 修改数据库记录
        category.name = form.name.data
        category.icon = form.icon.data
        db.session.add(category)
        db.session.commit()
        flash(f"修改成功")
        return redirect(url_for("admin.category"))
    return render_template("admin/category_form.html", form=form)


@bp.route('/category/del/<int:cate_id>')
@login_required
def category_del(cate_id):
    # 删除分类
    category = Category.query.get(cate_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        flash(f"分类>{category.name}删除成功")
        return redirect(url_for("admin.category"))


# --------------------------博客文章的查增删改-----------------------------------

@bp.route('/article')
@login_required
def article():
    # 查看分类
    page = request.args.get('page', 1, type=int)
    # 分页处理
    pagination = Post.query.order_by(-Post.add_date).paginate(page=page, per_page=5, error_out=False)
    post_list = pagination.items
    print("页对象的数据", post_list)
    return render_template('admin/article.html', post_list=post_list, pagination=pagination)


@bp.route('/article/add', methods=['GET', 'POST'])
@login_required
def article_add():
    # 增加文章
    form = PostForm()
    form.category_id.choices = [(v.id, v.name) for v in Category.query.all()]
    form.tags.choices = [(v.id, v.name) for v in Tag.query.all()]

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            desc=form.desc.data,
            has_type=form.has_type.data,
            category_id=int(form.category_id.data),
            content=form.content.data,
        )
        post.tags = [Tag.query.get(tag_id) for tag_id in form.tags.data]
        db.session.add(post)
        db.session.commit()
        flash(f'{form.title.data}文章添加成功')
        return redirect(url_for('admin.article'))
    return render_template('admin/article_form.html', form=form)


@bp.route('/article/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def article_edit(post_id):
    # 修改文章
    # 找出当前操作的文章记录  通过文章id查找
    post = Post.query.get(post_id)
    # 文章标签
    tags = [tag.id for tag in post.tags]
    # post.category.id 外键的作用
    form = PostForm(
        title=post.title, desc=post.desc,
        category_id=post.category.id, has_type=post.has_type.value,
        content=post.content, tags=tags
    )

    form.category_id.choices = [(v.id, v.name) for v in Category.query.all()]
    form.tags.choices = [(v.id, v.name) for v in Tag.query.all()]

    if form.validate_on_submit():
        post.title = form.title.data
        post.desc = form.desc.data
        post.has_type = form.has_type.data
        post.category_id = int(form.category_id.data)
        post.content = form.content.data
        post.tags = [Tag.query.get(tag_id) for tag_id in form.tags.data]
        db.session.add(post)
        db.session.commit()
        flash(f'{form.title.data}文章修改成功')
        return redirect(url_for('admin.article'))
    return render_template('admin/article_form.html', form=form)


@bp.route('/article/del/<int:post_id>', methods=['GET', 'POST'])
@login_required
def article_del(post_id):
    article = Post.query.get(post_id)
    if article:
        db.session.delete(article)
        db.session.commit()
        flash(f"{article.title}删除成功")
        return redirect(url_for("admin.article"))
    # return render_template("admin",form = form)


# -------------------------------标签管理-------------------------------------

@bp.route('/tag')
@login_required
def tag():
    page = request.args.get('page', 1, type=int)
    # 分页处理
    pagination = Tag.query.order_by(-Tag.add_date).paginate(page=page, per_page=10, error_out=False)
    tag_list = pagination.items
    return render_template('admin/tag.html', tag_list=tag_list, pagination=pagination)


@bp.route('/tag/add', methods=['GET', 'POST'])
@login_required
def tag_add():
    # 增加标签
    form = TagForm()
    if form.validate_on_submit():
        tag = Tag(name=form.name.data)
        db.session.add(tag)
        db.session.commit()
        flash(f'{form.name.data}添加成功')
        return redirect(url_for('admin.tag'))
    return render_template('admin/tag_form.html', form=form)


@bp.route('/tag/edit/<int:tag_id>', methods=['GET', 'POST'])
@login_required
def tag_edit(tag_id):
    # 修改标签
    tag = Tag.query.get(tag_id)
    form = TagForm(name=tag.name)
    if form.validate_on_submit():
        tag.name = form.name.data
        db.session.add(tag)
        db.session.commit()
        flash(f'{form.name.data}添加成功')
        return redirect(url_for('admin.tag'))
    return render_template('admin/tag_form.html', form=form)


@bp.route('/tag/del/<int:tag_id>', methods=['GET', 'POST'])
@login_required
def tag_del(tag_id):
    # 删除标签
    tag = Tag.query.get(tag_id)
    if tag:
        db.session.delete(tag)
        db.session.commit()
        flash(f'{tag.name}删除成功')
        return redirect(url_for('admin.tag'))