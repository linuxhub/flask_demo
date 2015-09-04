#encoding:utf8

from functools import wraps
from flask import abort
from flask.ext.login import current_user


#这是一个修饰器
#如果不是管理员用户则跳转到403页面
#使用方法,先引用,然后使用 @admin_required
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return func(*args, **kwargs)
    return wrapper







