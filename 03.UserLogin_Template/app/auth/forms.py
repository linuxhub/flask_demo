#encoding:utf8

'''  表单 '''


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, EqualTo, Regexp
from ..models import User



class LoginForm(Form):

              #邮件使用WTForms提供的Length()和Email()验证函数
              email = StringField(u'帐号', validators=[Required(), Length(1, 64), Email()])  #电子邮件文体字段

              #<input>元素
              password = PasswordField(u'密码', validators=[Required()])                  #密码字段

              #复选框
              remember_me = BooleanField(u'记住密码')   #记住我 复选框

              submit = SubmitField(u'登录')  #提交按钮


#修改密码
class ChangePasswordForm(Form):
              '''  修改密码 '''
              old_password = PasswordField(u'原密码', validators=[Required()])
              password = PasswordField(u'新密码', validators=[Required(), EqualTo('password2', message=u'您两次输入的新密码不一致')])
              password2 = PasswordField(u'重输密码',validators=[Required()])
              submit = SubmitField(u'更新密码')
