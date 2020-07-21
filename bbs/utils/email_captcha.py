import random
import string

def generate_random_str(randomlength=16):
    """
    random.chice(xxx):随机选择xxx的其中一个
    string.digits:0123456789
    string.ascii_letters:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    :param randomlength: 规定随机字符串的长度
    :return: 返回一个指定长度的随机字符串
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

# if __name__ == '__main__':
#     str = generate_random_str(randomlength=4)
#     print(str)