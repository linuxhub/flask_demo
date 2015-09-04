#encoding:utf8

'''  蓝本中定义路由程序  '''
from . import main      #main蓝本
from datetime import datetime
from flask import render_template, redirect, url_for, request
from flask.ext.login import  login_required


from flask.ext.login import current_user


#蓝本.路由
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():

    #响应请求
    user_agent = request.headers.get('User-Agent')

    #获取ip
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr


    return render_template('index.html',
                           current_time=datetime.now(),
                           user_agent=user_agent,
                           ip=ip
                           )






