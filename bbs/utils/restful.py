from flask import jsonify

class HttpCode(object):
    ok = 200
    paramerror = 400
    Unautherror = 401
    Forbiddenerror = 403
    servererror = 500

def success(message='',data=''):
    return jsonify({'code':200, 'message':message, 'data':data})


def param_error(message='',data=''):
    return jsonify({'code':400, 'message':message, 'data':data})


def Unauth_error(message='',data=''):
    return jsonify({'code':401, 'message':message, 'data':data})


def Forbidden_error(message='',data=''):
    return jsonify({'code':403, 'message':message, 'data':data})


def server_error(message='',data=''):
    return jsonify({'code':500, 'message':message or '页面出现了一些错误，请重新刷新', 'data':data})