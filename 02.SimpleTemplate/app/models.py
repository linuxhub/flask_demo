#encoding:utf8

'''  数据模型  '''

from . import db


#定义User模型
class User(db.Model):
              __tablename__ = 'users'                                       #表名
              id = db.Column(db.Integer, primary_key=True)                  #列名 用户id
              email = db.Column(db.String(64), unique=True, index=True)     #列名 email （用户使用电子邮件进行登录）
              username = db.Column(db.String(64), unique=True, index=True)  #列名 用户名
              password_hash = db.Column(db.String(128))                     #列名 密码哈希散列

              @property  #@property作用是将方法函数变成了属性
              def password(self):
                            '''  password的只读属性(如果试图读取password属性的值,则会返回错误)  '''
                            raise AttributeError(u'密码是不可读的属性')


              @password.setter
              def password(self, password):
                            ''' 使用generate_password_hash()函数,将原始密码作为输入,以字符串形式输出密码的散列值,
                                 将结果赋值给password_hash字段 '''
                            self.password_hash = generate_password_hash(password)


              def verify_password(self, password):
                            '''  接收密码,并与password_hash中的密码散列值进行对比,如果密码正确返回True '''
                            return check_password_hash(self.password_hash, password)

              def __repr__(self):
                  return '<User %r>' % self.username

