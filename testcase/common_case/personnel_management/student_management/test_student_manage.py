import json

import allure
import requests
from common.generate_data import *
from configer.log_config import get_logger
from configer.server_config import *

log = get_logger(__name__)


@allure.feature('feature学生管理')
@allure.story('story学生管理')
@allure.title('title学生管理')
@allure.description('description学生管理')
def test_index_lesson_live_init(login_organ):
    body = {"offset": 0, "pageSize": 10, "needTotalSize": True, "status": "1"}
    url = get_organ_http_server() + '/k12/org/student/manage'
    sv_params = get_user_params(login_organ)
    default_header = get_default_header()
    headers = generate_sv(default_header, sv_params)
    headers = add_content_type(headers)
    log.info(headers)
    response = requests.post(url=url, headers=headers, data=json.dumps(body), proxies=get_proxies())
    is_true = response.json()['success']
    if is_true is True:
        assert 1
    else:
        log.error(response.json())
        assert is_true is True
