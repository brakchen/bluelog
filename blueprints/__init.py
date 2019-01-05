from falsk import flask
from bluelog.settings import config
from bluelog.Blueprint.admin import admin_bp
from bluelog.Blueprint.auth import auth_bp
from bluelog.Blueprint.blog import blog_bp

config_name = os.getenv('FLASK_CONFIG', 'development')
app.config.from_object(config[config_name])


def create_app(config_name=None):
    if config_name if None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app
