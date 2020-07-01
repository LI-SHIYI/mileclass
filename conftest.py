import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

import pytest
import requests

from common.generate_data import *
from testdata.user_data import *
from configer.server_config import *
from configer.log_config import get_logger

log = get_logger(__name__)


@pytest.fixture(scope='session')
def login_organ():
    key_psw = 'password'
    url = get_organ_http_server() + '/k12/org/user/login'
    params = get_organ_login_params()
    en_psw = generate_psw(params.get(key_psw))
    params[key_psw] = en_psw
    default_header = get_default_header()
    headers = generate_sv(default_header, params)
    log.info(headers)

    response = requests.post(url=url, headers=headers, params=params, proxies=get_proxies())

    is_true = response.json()['success']

    if is_true is True:
        user_id = response.json()['object']['orgUserVo']['id']
        log.info('user_id=' + str(user_id))
        user_token = response.json()['object']['orgUserVo']['loginToken']
        log.info('user_token=' + user_token)
        return str(user_id), user_token
    else:
        log.error(response.json())
        return None, None
