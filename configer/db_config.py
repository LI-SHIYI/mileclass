def get_redis_config():
    host = '10.4.7.171'
    port = '6379'
    db = 'kzkt-qa'
    password = 'kzkt1234'
    return host, port, db, password


def get_k12_pg_config():
    database = 'kzkt'
    user = 'kzkt'
    password = 'kzkt'
    host = '10.4.7.199'
    port = '5432'
    return database, user, password, host, port


def get_room_pg_config():
    database = 'common_class'
    user = 'common_class',
    password = 'common_class2018'
    host = '10.4.7.199'
    port = '6531'
    return database, user, password, host, port
