from flask import Flask
from dashboard.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
from flask_socketio import SocketIO
from flask_mail import Mail

from blinker import Namespace

from dashboard.app.momentjs import momentjs


app = Flask(__name__, static_folder="\\projects\\new_renko\\dashboard\\static", static_url_path="")
#app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
socketio = SocketIO(app)
mail = Mail(app)

app_signals = Namespace()
config_changed = app_signals.signal('config-changed')
new_bot_created = app_signals.signal('new-bot-created')
get_bot_status = app_signals.signal('get-bot-status')
destroy_bot = app_signals.signal('stop-bot')

app.jinja_env.globals['momentjs'] = momentjs

from dashboard.app.authorizer import authorize, activation_type
app.jinja_env.globals['authorize'] = authorize
app.jinja_env.globals['activation_type'] = activation_type

from dashboard.app import routes, models, errors, websocket_server

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)