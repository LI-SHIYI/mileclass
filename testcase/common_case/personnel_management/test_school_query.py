import allure
import requests
from common.generate_data import *
from configer.log_config import get_logger
from configer.server_config import *

log = get_logger(__name__)


@allure.feature('feature学校查询')
@allure.story('story学校查询')
@allure.title('title学校查询')
@allure.description('description学校查询')
def test_index_lesson_live_init(login_organ):
    url = get_organ_http_server() + '/k12/org/school/query'
    sv_params = get_user_params(login_organ)
    default_header = get_default_header()
    headers = generate_sv(default_header, sv_params)
    log.info(headers)
    response = requests.get(url=url, headers=headers, proxies=get_proxies())
    is_true = response.json()['success']
    if is_true is True:
        assert 1
    else:
        log.error(response.json())
        assert is_true is True
