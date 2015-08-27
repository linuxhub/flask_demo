#encoding:utf8

''' auth 蓝本中的路由和视图函数  '''

from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, ChangePasswordForm


from flask import  render_template, redirect, request, url_for, flash, current_app, abort
from flask.ext.login import login_user, logout_user, login_required, current_user




#用户登录
@auth.route('/login', methods=['GET', 'POST']) # /login路由
def login():
              '''  用户登录  '''
              form = LoginForm()
              if form.validate_on_submit():
                            user = User.query.filter_by(email=form.email.data).first()

                            #如果邮件地址对应的用户存在,再调用用户对象的verify_password(密码)方法.
                            if user is not None and user.verify_password(form.password.data):

                                          #如果密码正确,则调用login_user()函数,在用户会话中把用户标记为已登录
                                          login_user(user, form.remember_me.data)

                                          return redirect(request.args.get('next') or url_for('main.index'))

                            #密码不正确,提示消息
                            flash(u'用户名或密码错误.')

              return render_template('auth/login.html', form=form)   #模板文件保存在: app/templates/auth/login.html



#用户资料页面的路由
@auth.route('/user/<username>')
def user(username):
              user = User.query.filter_by(username=username).first()
              #如果用户不存在则返回404错误
              if user is None:
                            abort(404)
              return render_template('auth/user.html', user=user)


#用户退出
@auth.route('/logout')
@login_required
def logout():
              ''' 用户退出 '''
              logout_user() #删除并重设用户会话
              flash(u'用户已退出') #提示消息
              return redirect(url_for('main.index')) #重定向到首页



#更改密码
@auth.route('/change-password', methods=['GET','POST'])
@login_required
def change_password():
              form = ChangePasswordForm()
              if form.validate_on_submit():
                            #判断原始密码是否正确(如果正确赋值)
                            if current_user.verify_password(form.old_password.data):
                                          current_user.password = form.password.data
                                          db.session.add(current_user)
                                          flash(u'密码已更改.')
                                          return redirect( url_for('auth.user', username=current_user.username) )
                            else:
                                          flash(u'原始密码错误')
              return render_template("auth/change_password.html", form=form)