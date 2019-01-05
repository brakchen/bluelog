from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLALchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment


bootstrap = Bootstrap()
db = SQLALchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
