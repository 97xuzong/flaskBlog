from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from .settings import BASE_DIR
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # 默认从文件加载配置
    app = Flask(__name__, instance_relative_config=True)

    # # 默认配置
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # 判断是否传入配置
    if test_config is None:
        db_config_base = BASE_DIR / "RealProject/settings.py"
        app.config.from_pyfile(db_config_base, silent=True)
    else:
        # 如果有指定配置文件  则按照指定来
        app.config.from_mapping(test_config)

    # 配置完app，初始化数据库
    db.init_app(app)

    # 实例化迁移实例
    migrate.init_app(app, db)

    # 注册蓝图对象
    from app.blog import bp as blog_bp
    from app.auth.views import bp as auth_bp
    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp)
    from app.blog import models
    from app.auth.models import auth
    return app
