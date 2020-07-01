from configer.server_config import is_release_environment


def get_organ_login_params():
    if is_release_environment():
        return {
            "username": "breeze",
            "password": "000000p"
        }
    else:
        return {
            "username": "breezezheng",
            "password": "000000p"
        }
