from wtforms import Form,StringField,PasswordField
from wtforms.validators import Length,NumberRange ,DataRequired,Email,ValidationError
from app.models.user import User
class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='邮箱长度应在8-64位之间')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空，请输入密码'),Length(6,32,message='密码长度应在6-32位之间')])
    nickname = StringField(validators=[DataRequired(),Length(2,10,message='昵称长度应在2-10位之间')])
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():  #判断email是否重复
             raise ValidationError('该邮箱已被注册！')
             
    def validate_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():  #判断nickname是否重复
             raise ValidationError('该昵称已被使用！')
             
class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message='邮箱长度应在8-64位之间')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空，请输入密码'),Length(6,32,message='密码长度应在6-32位之间')])