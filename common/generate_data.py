import ctypes
import datetime
import hashlib
import time


def generate_psw(psw):
    """
    :return: 返回加密后的密码
    """
    m = hashlib.md5()
    b = ("rCt52pF2cnnKNB3Hkp" + psw).encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


def generate_sv(default_header, custom_param):
    """
    :return: 生成sv，并返回拼接后的完整headers
    """
    default_header.update(custom_param)
    keys = list(default_header.keys())
    keys.sort()
    # create the string to be signed
    valuesStr = ''
    for key in keys:
        if default_header[key]:
            valuesStr += str(default_header[key]).lower()
    if len(valuesStr) < 8:
        valuesStr += '0123456789012345'
    # 排序序列
    s1 = [0 * i for i in range(0, 8)]
    for i in range(0, len(valuesStr) // 8 - 1):
        for j in range(0, 8):
            if (i + 1) * 8 + j < len(valuesStr):
                if i == 0:
                    s1[j] = ord(valuesStr[i * 8 + j])
                s1[j] ^= ord(valuesStr[(i + 1) * 8 + j])
    # encode the bytes to string
    encodeStr = ''
    # 排序密码表
    HEX_TAB_WEB = "s~0!e@5#c$8%r^6&"
    sum = 0
    for i in range(0, 8):
        # 获取密码指针
        r1 = unsigned_right_shitf(s1[i], 3) & 0xF
        r2 = s1[i] & 0xF
        tempS = HEX_TAB_WEB[r1] + HEX_TAB_WEB[r2]
        encodeStr += tempS
        sum += ord(HEX_TAB_WEB[r1])
    # 末尾两个干扰码
    encodeStr += HEX_TAB_WEB[sum % 16]
    encodeStr += HEX_TAB_WEB[sum % 13]
    default_header['s'] = encodeStr
    return default_header


def int_overflow(val):
    # 因python左移没有溢出的概念，int左移如果溢出会自动变为long型，所以手动写一个左移溢出
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shitf(n, i):
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    # print(n)
    return int_overflow(n >> i)


def generate_current_time():
    """
    :return: 获取当前时间（毫秒）
    """
    return int(round(time.time() * 1000))


def generate_today_end_time():
    """
    :return: 获取今天的结束时间（毫秒）
    """
    return generate_today_start_time() + 24 * 60 * 60 * 1000 - 2


def generate_today_start_time():
    """
    :return: 获取今天的开始时间（毫秒）
    """
    return int(time.mktime(datetime.date.today().timetuple()) * 1000)


def generate_today_query_time():
    return {
        "queryTimeStart": str(generate_today_start_time()),
        "queryTimeEnd": str(generate_today_end_time())
    }


def get_user_params(login):
    user_id, user_token = login
    return {
        "loginUserId": user_id,
        "loginToken": user_token
    }
