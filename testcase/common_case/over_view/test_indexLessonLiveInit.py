import allure
import requests
from common.generate_data import *
from configer.log_config import get_logger
from configer.server_config import *

log = get_logger(__name__)


@allure.feature('feature今日上课情况接口用例')
@allure.story('story今日上课情况接口用例')
@allure.title('title今日上课情况接口用例')
@allure.description('description今日上课情况接口用例')
def test_index_lesson_live_init(login_organ):
    # /k12/org/org/indexLessonLiveInit?queryTimeStart=1587520800000&queryTimeEnd=1587544144169
    url = get_organ_http_server() + '/k12/org/org/indexLessonLiveInit'
    sv_params = get_user_params(login_organ)
    default_header = get_default_header()
    param = generate_today_query_time()
    sv_params.update(param)
    headers = generate_sv(default_header, sv_params)
    log.info(headers)
    response = requests.get(url=url, headers=headers, params=param, proxies=get_proxies())
    is_true = response.json()['success']
    if is_true is True:
        assert 1
    else:
        log.error(response.json())
        assert is_true is True
