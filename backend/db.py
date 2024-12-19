import os
import mysql.connector
from mysql.connector import pooling

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

# MySQLコネクタプールを作成
db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)


def get_db_connection():
    return db_pool.get_connection()
