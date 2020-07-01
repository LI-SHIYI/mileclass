from common.generate_data import generate_current_time


def is_release_environment():
    """
    :return: True = 机构管理后台正式环境
    """
    # is_release = True
    is_release = False
    return is_release


def get_organ_http_server():
    """
    :return: 机构管理后台的api地址
    """
    if is_release_environment():
        return 'http://service.mileedu.cn'
    else:
        return 'http://10.4.7.243'


def get_organ_d():
    """
    :return: 机构管理后台的机构域名
    """
    if is_release_environment():
        return "intest.mileclass.cn"
    else:
        return "breezezheng.mileclass.cn"


def get_default_header():
    return {
        "p": '11',
        "c": '-1',
        "v": "0.0.1",
        "d": get_organ_d(),
        "t": str(generate_current_time())
    }


def get_go_native():
    """
    :return: True=走本地代理，可用于fiddler抓包
    """
    return False


def get_proxies():
    """
    :return: 返回本地代理，根据实际情况修改
    """
    if get_go_native() is True:
        return {'http': 'http://10.0.30.232:8888', 'https': 'http://10.0.30.232:8888'}
    else:
        return None


def add_content_type(headers):
    """
    :return: 增加content-type,并返回
    """
    headers['Content-Type'] = "application/json"
    return headers
