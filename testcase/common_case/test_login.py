import allure


@allure.feature('feature用户登录用例')
@allure.description('description用户登录用例')
@allure.story('story用户登录用例')
@allure.title('title用户登录用例')
def test_login(login_organ):
    uid, token = login_organ
    assert uid is not None and token is not None
    pass
