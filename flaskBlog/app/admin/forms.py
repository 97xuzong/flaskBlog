#  -*- coding: utf-8 -*-
# @Author  : ymnl
# @File    : forms.py
# @Time    : 2022/11/22 9:48
# @Software: PyCharm
# @function: 分类有关表单验证

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField, TextAreaField, SelectMultipleField, \
    BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo

from app.blog.models import PostPublishType


class CategoryForm(FlaskForm):
    name = StringField('name', validators=[
        DataRequired(message="不能为空"),
        Length(max=32, message="不符合字数要求！")
    ])
    icon = StringField('icon', validators=[
        DataRequired(message="不能为空"),
        Length(max=32, message="不符合字数要求！")
    ])


class PostForm(FlaskForm):
    # 添加文章表单
    title = StringField('标题', validators=[
        DataRequired(message="不能为空"),
        Length(max=128, message="不符合字数要求！")
    ])
    desc = StringField('描述', validators=[
        DataRequired(message="不能为空"),
        Length(max=200, message="不符合字数要求！")
    ])
    has_type = RadioField('发布状态',
                          choices=(PostPublishType.draft.name, PostPublishType.show.name),
                          default=PostPublishType.show.name)
    category_id = SelectField(
        '分类',
        choices=None,
        coerce=int,
        validators=[
            DataRequired(message="不能为空"),
        ]
    )
    content = TextAreaField('文章详情',
                            validators=[DataRequired(message="不能为空")]
                            )
    tags = SelectMultipleField('文章标签', choices=None, coerce=int)


class TagForm(FlaskForm):
    # 标签表单
    name = StringField('标签', validators=[
        DataRequired(message="不能为空"),
        Length(max=128, message="不符合字数要求！")
    ])


from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class CreateUserForm(FlaskForm):
    # 创建表单
    username = StringField('username', validators=[
        DataRequired(message="不能为空"),
        Length(max=32, message="不符合字数要求！")
    ])
    password = PasswordField('password', validators=[
        # DataRequired(message="不能为空"),
        Length(max=32, message="不符合字数要求！")
    ], description="修改用户信息时，留空则代表不修改！")
    avatar = FileField("avatar", validators=[
        # FileRequired(),
        FileAllowed(['jpg', 'png', 'gif'], message="仅支持jpg/png/gif格式"),
        FileSize(max_size=2048000, message="不能大于2M")],
                       description="大小不超过2M，仅支持jpg/png/gif格式，不选择则代表不修改")
    is_super_user = BooleanField("是否为管理员")
    is_active = BooleanField("是否活跃", default=True)
    is_staff = BooleanField("是否锁定")
