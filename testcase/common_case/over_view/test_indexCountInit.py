import allure
import requests
from common.generate_data import *
from configer.log_config import get_logger
from configer.server_config import *

log = get_logger(__name__)


@allure.feature('feature今日上课课次数量')
@allure.story('story今日上课课次数量')
@allure.title('title今日上课课次数量')
@allure.description('description今日上课课次数量')
def test_index_count_init(login_organ):
    url = get_organ_http_server() + '/k12/org/org/indexCountInit'
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
