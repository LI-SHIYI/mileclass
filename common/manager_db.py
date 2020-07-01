import psycopg2 as psycopg2
from redis import StrictRedis
from configer.db_config import *
from configer.log_config import get_logger

log = get_logger(__name__)


def execute_k12_pg_db(sql, is_k_12):
    """
    :param sql: sql语句
    :return:执行结果
    """
    rows = None
    if sql is None:
        return rows
    if is_k_12:
        database, user, password, host, port = get_k12_pg_config()
    else:
        database, user, password, host, port = get_room_pg_config()
    try:
        connection = psycopg2.connect(database=database,
                                      user=user, password=password, host=host,
                                      port=port)
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.close()
    except Exception as e:
        log.error(e)
    return rows


def execute_redis_db(key):
    """
    :param key: 要查的key值
    :return:查到的结果
    """
    value = None
    if key is None:
        return value
    try:
        host, port, db, password = get_redis_config()
        redis_pool = StrictRedis(host=host, port=port, db=db, password=password)
        log.error(redis_pool.keys())
        value = redis_pool.get(key)
    except Exception as e:
        log.error(e)
    return value
