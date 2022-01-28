import pytest
import logging
import psycopg2
import os
# from onesixpiece import PGAdaptor

pytest.main(args=['-s', os.path.abspath(__file__)])
logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s- %(message)s"
)

given = pytest.mark.parametrize
skipif = pytest.mark.skipif
skip = pytest.mark.skip
xfail = pytest.mark.xfail

postgres_host = "192.168.2.13"               # 数据库地址
postgres_port = "5432"       # 数据库端口
postgres_user = "user"              # 数据库用户名
postgres_password = "password"      # 数据库密码
postgres_datebase = "sandbox"      # 数据库名字
conn_string = "host=" + postgres_host + " port=" + postgres_port + " dbname=" + postgres_datebase + \
                        " user=" + postgres_user + " password=" + postgres_password



# @pytest.mark.usefixtures("connect_pg")
class TestPGAdatorClass:
    conn = None
    @pytest.fixture(scope="module")
    def conn(self):
        logging.info("Run fixture setup")
        conn = psycopg2.connect(conn_string)
        yield conn
        logging.info("Team down")
        conn.close()


    def test_connect(self, conn):
        # connection string
        # conn = psycopg2.connect(conn_string)
        logging.info("start to run test_connect")
        assert conn is not None


    def create_table(self):
        assert True

    # def test_insertdata(self):
    #     assert True


    # def test_updatedata(self):
    #     assert True

    # def test_delete(self):
    #     assert True


if __name__ == '__main__':
    pytest.main(args=['-s', os.path.abspath(__file__)])
