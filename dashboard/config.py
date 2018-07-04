import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "autobotcloudabc@gmail.com"
    MAIL_PASSWORD = "kesh2828"

    SECURITY_PASSWORD_SALT = "$2b$12$UoI9MPk8Z5C54aliCZxTyu"

    RECAPTCHA_PUBLIC_KEY = "6LdQemAUAAAAAMHl64OR_uzU8Cde9l_iIO8mzjFi"
    RECAPTCHA_PRIVATE_KEY = "6LdQemAUAAAAAPhsgYHuqYC5mvR0CzqfN502RuFF"

    ADMINS = ['autobotcloudabc@gmail.com']
    DEBUG = True

    HMAC_KEY = "Gmc8gWKlZGaxipc4lww12g"