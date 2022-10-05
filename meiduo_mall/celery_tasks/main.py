# celery 入口
from celery import Celery

# 为celery使用django配置文件进行设置
import os

# celery环境与django独立，所以无法加载到settings文件，因此要在入口文件处配置settings位置
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'

# 创建celery实例对象
celery_app = Celery('meiduo')

# 加载celery配置
celery_app.config_from_object('celery_tasks.config')

# 自动注册celery任务
celery_app.autodiscover_tasks(['celery_tasks.sms', 'send_verify_email'])
