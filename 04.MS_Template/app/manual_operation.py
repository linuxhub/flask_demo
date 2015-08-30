#encoding:utf8

'''  这是一个手动操作 执行文件  比如需要手动初始化增加一些用户  '''

from . import db
from .models import User



class Manual():
              
              def __init__(self):
                            pass          
              
              @staticmethod
              def create_default_user_admin():
                            '''  创建默认管理员用户
                                 用户名: admin  密码： admin 
                            '''
                            email='root@linuxhub.org'
                            username='root'
                            password='root'
                            is_admin=1
                            
                            #判断登录邮箱是否存,如果存在则删除该用户，重新创建用户;
                            if User.query.filter_by(email=email).first():
                                          User.query.filter(User.email == email).delete()
                                          #db.session.commit()  
                                          print "delete %s user ok" % username
                                          user = User(email=email,username=username,password=password,is_admin=is_admin)
                                          db.session.add(user)
                                          #db.session.commit() 
                                          print "create %s user ok" % username
                                          print "\n----------------------"
                                          print " email: %s \n password: %s" % (email,password)
                                          print "----------------------\n"
                            else:
                                          user = User(email=email,username=username,password=password,is_admin=is_admin)
                                          db.session.add(user)
                                          db.session.commit()
                                          print "create %s user ok" % username
                                          print "\n----------------------"
                                          print " email: %s \n password: %s" % (email,password)
                                          print "----------------------\n"