from wtforms import Form
from wtforms import StringField
from wtforms.validators import regexp, InputRequired
import hashlib

class BaseError(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message


class SmsCaptchaForm(Form):
    telephone = StringField(validators=[regexp(r'1[3456789]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired()])

    # 拿前端发送过来的sign和后端加密过的sign2来做对比
    def validate_sign(self,field):
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        # 服务器端加密的sign
        sign2 = hashlib.md5((timestamp + telephone + 'q3423805gdflvbdfvhsdoa`#$%').encode('utf-8')).hexdigest()

        if sign2 == sign:
            return True
        else:
            return False