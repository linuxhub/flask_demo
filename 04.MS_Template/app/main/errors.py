#encoding:utf8

'''
    蓝本中定义错误处理程序
    自定义错误页面 
'''

from flask import render_template
from . import main
from flask.ext.login import  login_required



#禁用访问
@main.app_errorhandler(403)
def internal_server_error(e):
    return render_template('403.html'), 403



#404, 客户端请求未知页面或路由时显示
@main.app_errorhandler(404)
@login_required #如果用户没有登录会挑转到用户登录页面
def page_not_found(e):
            return render_template('404.html'), 404


#500, 有未处理的异常时显示
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

