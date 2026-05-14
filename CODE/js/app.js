from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'securecodingsecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

DB = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from routes.auth_routes import *
from routes.dashboard_routes import *
from routes.upload_routes import *
from routes.analysis_routes import *
from routes.report_routes import *

if __name__ == '__main__':
    with app.app_context():
        DB.create_all()
    app.run(debug=True)