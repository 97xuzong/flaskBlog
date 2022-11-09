from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

SECRET_KEY = 'xuzong'

SQLALCHEMY_DATABASE_URI = 'mysql://root:xz123@127.0.0.1:3306/flaskblog'

SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
