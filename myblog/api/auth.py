from functools import wraps
from flask import Blueprint, g, request
from flask_httpauth import HTTPBasicAuth
from ..db.models import User


prefix = '/api/v1/auth'
bp = Blueprint('auth', __name__, url_prefix=prefix)
auth = HTTPBasicAuth()

# login
@auth.verify_password
def verify_password(username_or_token, password):
    if request.path == prefix+"/login":
        user = User.query.filter_by(name=username_or_token).first()
        if user.password != password:
            return False
    else:
        user = User.verify_auth_token(username_or_token)
        if not user:
            return False
    g.user = user
    return True

@bp.route('/login',methods=['POST'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return {"token":token,"user":g.user}

def permission_required(permission):
  def decorator(f):
      @wraps(f)
      def wrapper(*args, **kwargs):
          if permission=='owner':
              if g.user.name=='root':
                  return f(*args, **kwargs)
              else:
                  return 'no permission'
          else:
              return 'no permission'
      return wrapper
  return decorator
