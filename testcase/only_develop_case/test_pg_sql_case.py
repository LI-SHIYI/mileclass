import allure

from common.manager_db import execute_k12_pg_db
from configer.log_config import get_logger
from testdata.user_data import get_organ_login_params

log = get_logger(__name__)


@allure.feature('feature pg sql case demo')
@allure.story('story pg sql case demo')
@allure.title('title pg sql case demo')
@allure.description('description pg sql case demo')
def test_index_count_init(login_organ):
    user_id, username = login_organ
    params = get_organ_login_params()
    login_username = params.get('username')
    db_id = execute_k12_pg_db("select id from uc_user_register where username = '" + login_username + "'", True)
    if str(user_id) == str(db_id[0][0]):
        assert 1
    else:
        log.error(db_id[0])
        assert 0
