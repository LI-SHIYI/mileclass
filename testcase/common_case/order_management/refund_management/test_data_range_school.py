import allure
import requests
from common.generate_data import *
from configer.log_config import get_logger
from configer.server_config import *

log = get_logger(__name__)


@allure.feature('feature加载初始化学校列表')
@allure.story('story加载初始化学校列表')
@allure.title('title加载初始化学校列表')
@allure.description('description加载初始化学校列表')
def test_index_lesson_live_init(login_organ):
    url = get_organ_http_server() + '/k12/admin/dataAuth/dataRangeSchool'
    sv_params = get_user_params(login_organ)
    default_header = get_default_header()
    headers = generate_sv(default_header, sv_params)
    log.info(headers)
    response = requests.get(url=url, headers=headers, proxies=get_proxies())
    is_true = response.json()['success']
    if is_true is True:
        log.error(response.json())
        assert 0
    else:
        log.error(response.json())
        assert is_true is True
