import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRERT_KEY = 'my_precious'
SQL_ALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'nwblog.sqlite')
