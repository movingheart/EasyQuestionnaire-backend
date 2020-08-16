# @Time    : 2020/3/7 13:32
# @Author  : yuzhanglong
# @Email   : yuzl1123@163.com
from app.utils.templateMaker.templateMaker import pushWJWDataToDB


class Config:
    # 创建秘钥
    SECRET_KEY = 'yzl'

    # jsonify配置
    JSON_AS_ASCII = False

    # token过期时间
    TOKEN_EXPIRATION = 7200

    # 邮件配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = '1877515277@qq.com'
    MAIL_PASSWORD = 'jiyihuhfdvqncedi'
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = '1877515277@qq.com'
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False

    # 管理员邮箱(自行设定，用来发送一些任务完成信息 例如爬虫任务)
    ADMIN_EMAIL = "yuzl1123@163.com"

    # 模板管理用户的用户名(该用户下的所有问卷都是模板 便于管理 如果不存在会自动创建一个)
    TEMPALTES_MANAGER = "TEMPLATE_MAKER"

    # 微信小程序相关
    # APP_ID
    MINI_PROGRAM_APPID = "这里填写微信小程序appid"
    MINI_PROGRAM_APPSECRET = "这里填写小程序appsecret"


class DevelopmentConfig(Config):
    # mongodb 配置
    MONGODB_SETTINGS = {
        'db': 'questionnaire-test-new',
        'host': 'mongodb://localhost/questionnaire-test-new'
    }

    # 开发环境下web端的url
    WEB_BASE_URL = "http://127.0.0.1:8080"
    DEBUG = True


class ProductionConfig(Config):
    # mongodb 配置
    MONGODB_SETTINGS = {
        'db': 'questionnaire',
        'host': 'mongodb://localhost/questionnaire'
    }

    # 生产环境下web端的url
    WEB_BASE_URL = "http://wenjuan.yuzzl.top"

    # 定时任务相关
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            "id": "runTask",  # 任务ID
            "func": pushWJWDataToDB,  # 任务位置
            "trigger": "cron",  # 触发器
            "hour": '16',  # 时间
            "minute": '38'
        }
    ]
